import argparse
import nltk
import os
import pywhisper
import subprocess
import tempfile
import shutil
import urllib3
import warnings
import tkinter as tk

from dotenv import load_dotenv
from nltk.tokenize import sent_tokenize
from tkinter import filedialog

load_dotenv()
nltk.download('punkt')
warnings.filterwarnings("ignore", category=UserWarning)

global ffmpegpath
ffmpegpath = None

if os.name == 'nt':
    # Windows
    ffmpegpath = r"./ffmpeg.exe"
elif os.name == 'posix':
    ffmpegpath = "ffmpeg"


def download_ffmpeg():
    if os.name == 'nt':
        """Download ffmpeg from specified URL and extract the *.exe files into the root of the project directory."""
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z"
        temp_dir = os.path.join(os.getcwd(), ".temp")
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, "ffmpeg.7z")
        urllib3.request.urlretrieve(url, file_path)
        subprocess.run(["7z", "x", file_path, "-o" + temp_dir])
        bin_dir = os.path.join(temp_dir, "ffmpeg-git-essentials", "bin")
        for file in os.listdir(bin_dir):
            if file == ("ffmpeg.exe"):
                shutil.copy(os.path.join(bin_dir, file), os.getcwd())
        shutil.rmtree(temp_dir, ignore_errors=True)
    elif os.name == 'posix':
        print("Please install ffmpeg and add it to your system's PATH environment variable, then restart this script.")
        exit(1)


def check_ffmpeg():
    """Check if ./ffmpeg.exe exists, if not download from specified URL and extract the *.exe files into the root of the project directory."""
    global ffmpegpath
    if ffmpegpath is None or not os.path.exists(str(ffmpegpath)):
        download_ffmpeg()
    elif os.name == 'posix':
        try:
            subprocess.run(["ffmpeg", "-version"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            print("Please install ffmpeg and add it to your system's PATH environment variable, then restart this script.")
            exit(1)
        else:
            ffmpegpath = "ffmpeg"


def convert_to_wav(file, output_file):
    """Convert mp3 to wav using ffmpeg."""
    check_ffmpeg()
    command = [ffmpegpath, '-i', file, '-acodec',
               'pcm_u8', '-ar', '22050', output_file]
    with open(os.devnull, 'w') as devnull:
        subprocess.run(command, stdout=devnull, stderr=devnull)


def transcribe(file):
    """Transcribe audio file using pywhisper."""
    model_name = os.getenv('model_name') or "tiny"
    model = pywhisper.load_model(model_name)
    result = model.transcribe(file)
    return result["text"]


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Transcribe audio files.')
    parser.add_argument('-d', '--destination', type=str,
                        help='Specify destination folder')
    parser.add_argument('-f', '--files', nargs='+',
                        help='Specify input file(s)')
    args = parser.parse_args()

    if args.destination:
        os.makedirs(args.destination, exist_ok=True)
    else:
        root = tk.Tk()
        root.withdraw()
        args.destination = filedialog.askdirectory()
        os.makedirs(args.destination, exist_ok=True)

    if args.files:
        files = args.files
    else:
        root = tk.Tk()
        root.withdraw()
        files = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])

    with tempfile.TemporaryDirectory(dir=args.destination) as temp_dir:
        for file in files:
            print(f'Processing {file}...')
            wav_file = os.path.join(temp_dir, os.path.splitext(
                os.path.basename(file))[0] + '.wav')
            print('Converting to wav...')
            convert_to_wav(file, wav_file)
            print('Transcribing...')
            transcription = transcribe(wav_file)
            sentences = sent_tokenize(transcription)
            with open(os.path.join(args.destination, os.path.splitext(os.path.basename(file))[0] + '.txt'), 'w') as f:
                for sentence in sentences:
                    f.write(sentence + '\n')
            print('Finished transcribing.')
            print('Transcription saved to ' + os.path.join(args.destination,
                  os.path.splitext(os.path.basename(file))[0] + '.txt'))
    shutil.rmtree(os.path.join(args.destination,
                  '.temp'), ignore_errors=True)


if __name__ == '__main__':
    main()

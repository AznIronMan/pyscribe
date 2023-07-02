# PyScribe

by [ClarkTribeGames, LLC](https://www.clarktribegames.com/)

PyScribe is a command-line tool to transcribe audio files. It uses `ffmpeg` for audio conversion and `pywhisper` for transcription.

## Prerequisites

1. Python 3.x
2. [FFmpeg](https://ffmpeg.org/download.html) (need the `ffmpeg` and `ffprobe` executables in the root of the project)

## Installation

1. Clone the repository or download the script to your local machine.

```bash
git clone https://github.com/AznIronMan/pyscribe
```

2. Navigate to the directory containing the script.
3. Install the required Python packages with `pip install -r requirements.txt` (you need to create this file and list `pywhisper` and `nltk` there).

## Usage

PyScribe can be run from the command line with the following options:

- `-d`: Specify the destination folder for the transcribed files.
- `-f`: Specify the input audio file(s) to transcribe.

If no destination folder is specified, the program will ask the user to select a folder. If no files are specified, the program will ask the user to select the files to transcribe.

NOTE: If using a headless or ssh environment, the folder/file selection will not work. You must use the `-d` and `-f` switches for this to work.

### Examples:

To transcribe a single file and save the output to a specific folder:

```bash
python pyscribe.py -f /path/to/audio/file.mp3 -d /path/to/output/folder
```

To transcribe multiple files:

```bash
python pyscribe.py -f /path/to/audio/file1.mp3 /path/to/audio/file2.mp3 -d /path/to/output/folder
```

If you do not specify any files or destination folder, the program will ask you to select them:

```bash
python pyscribe.py
```

## Requirements.txt

Be sure before trying to run the script to run `pip install -r requirements.txt` to install all prerequisites.

In case the 'requirements.txt' is missing for some reason, here is an export of the file as of 2023.07.01:

```bash
certifi==2023.5.7
charset-normalizer==3.1.0
click==8.1.3
colorama==0.4.6
decorator==4.4.2
filelock==3.12.2
fsspec==2023.6.0
huggingface-hub==0.15.1
idna==3.4
imageio==2.31.1
imageio-ffmpeg==0.4.8
Jinja2==3.1.2
joblib==1.3.1
MarkupSafe==2.1.3
more-itertools==9.1.0
moviepy==1.0.3
mpmath==1.3.0
networkx==3.1
nltk==3.8.1
numpy==1.25.0
packaging==23.1
Pillow==10.0.0
proglog==0.1.10
python-dotenv==1.0.0
pywhisper==1.0.6
PyYAML==6.0
regex==2023.6.3
requests==2.31.0
safetensors==0.3.1
sympy==1.12
tk==0.1.0
tokenizers==0.13.3
torch==2.0.1
tqdm==4.65.0
transformers==4.30.2
typing_extensions==4.7.0
urllib3==2.0.3
```

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contact

For any queries or concerns, please contact Geoff Clark at geoff @ clarktribegames . com.

# BGground

A free, fast, and AI-powered Image Background Remover web app built with HTML, CSS, and JavaScript. Instantly remove image backgrounds online with one click, no sign-up or software needed. Perfect for designers, creators, and e-commerce users.

## Transcription CLI

This repository now also provides a simple Python-based CLI that converts any video or audio file into a DOCX document containing the full transcription using OpenAI Whisper.

### Prerequisites

- Python 3.8+
- `ffmpeg` installed and available on PATH

### Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Usage

```bash
python transcribe.py path/to/video.mp4 --model base --output transcript.docx
```

- `--model` is optional and defaults to `base` (choices: `tiny`, `base`, `small`, `medium`, `large`).
- `--output` is optional; if omitted the DOCX will be written alongside the input with the same name.

### Notes

- The first run downloads the Whisper model; subsequent runs reuse the cached weights.
- Large models require more memory and GPU resources.
- Audio extracted from videos is processed via MoviePy and PyDub to ensure Whisper-compatible 16kHz mono WAV input.

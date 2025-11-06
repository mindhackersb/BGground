# Quick Start Guide - Video to Text Converter

Get started with the Video to Text Converter in just a few minutes!

## Installation

### 1. Install Dependencies

```bash
python3 -m pip install --user -r requirements.txt
```

This installs:
- `moviepy` - Video processing
- `SpeechRecognition` - Speech-to-text conversion
- `python-docx` - DOCX document generation
- `pydub` - Audio processing

### 2. Verify Installation

```bash
python3 video_to_text.py --help
```

If you see the help message, you're ready to go!

## Basic Usage

### Convert a Single Video

```bash
python3 video_to_text.py your_video.mp4
```

This will create `your_video.docx` with the full transcription.

### Specify Output File

```bash
python3 video_to_text.py meeting.mp4 -o meeting_notes.docx
```

### Convert Non-English Video

For Spanish:
```bash
python3 video_to_text.py video.mp4 -l es-ES
```

For French:
```bash
python3 video_to_text.py video.mp4 -l fr-FR
```

## Batch Processing

Convert multiple videos at once:

```bash
python3 batch_convert.py /path/to/videos/
```

With custom output directory:
```bash
python3 batch_convert.py videos/ -o transcripts/
```

Search subdirectories:
```bash
python3 batch_convert.py videos/ -r
```

Convert all AVI files:
```bash
python3 batch_convert.py videos/ -p "*.avi"
```

## Common Issues

### "No module named 'moviepy'"
Run: `python3 -m pip install --user moviepy==1.0.3`

### "No audio track found"
Your video file doesn't have audio. Ensure the video has an audio track.

### "Could not understand audio"
- Check audio quality in the video
- Ensure speech is clear
- Verify correct language code
- Reduce background noise

### Connection errors
Requires internet connection for Google Speech Recognition API.

## What You Get

The output DOCX file includes:
- Professional title and formatting
- Video metadata (filename, date, language)
- Complete transcription with proper paragraphs
- Clean, readable formatting

## Example Workflow

1. Record or download a video with speech
2. Run: `python3 video_to_text.py video.mp4`
3. Wait for processing (30-second video = ~1-2 minutes)
4. Open the generated `.docx` file
5. Review and edit the transcription as needed

## Tips for Best Results

1. Use high-quality video files
2. Ensure clear audio with minimal background noise
3. Use the correct language code
4. For long videos, be patient - processing takes time
5. Review transcription for accuracy

## Need More Help?

See the full documentation: `VIDEO_CONVERTER_README.md`

## Quick Reference

| Task | Command |
|------|---------|
| Convert single video | `python3 video_to_text.py video.mp4` |
| Custom output | `python3 video_to_text.py video.mp4 -o output.docx` |
| Spanish video | `python3 video_to_text.py video.mp4 -l es-ES` |
| Batch convert | `python3 batch_convert.py videos/` |
| Help | `python3 video_to_text.py --help` |

---

Ready to convert your first video? Just run:

```bash
python3 video_to_text.py your_video.mp4
```

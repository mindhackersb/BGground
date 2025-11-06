# Video to Text Converter - Project Structure

## Overview

This is a complete Python-based video-to-text converter agent that processes any video file and generates a professionally formatted DOCX document with the full transcription.

## Project Files

### Main Scripts

#### `video_to_text.py` (Main Script)
The core video-to-text converter with the following features:
- Extracts audio from any video format (MP4, AVI, MOV, MKV, etc.)
- Transcribes speech to text using Google Speech Recognition
- Generates professionally formatted DOCX documents
- Handles long videos by processing in chunks
- Command-line interface with customizable options
- Automatic cleanup of temporary files

**Usage:**
```bash
python3 video_to_text.py video.mp4
python3 video_to_text.py video.mp4 -o output.docx -l en-US
```

#### `batch_convert.py` (Batch Processor)
Batch process multiple video files at once:
- Process entire directories of videos
- Recursive directory search option
- Custom output directory support
- File pattern matching (e.g., *.mp4, *.avi)
- Progress tracking and error reporting
- Summary statistics

**Usage:**
```bash
python3 batch_convert.py videos/
python3 batch_convert.py videos/ -o transcripts/ -r
```

#### `example_usage.py` (Examples)
Example code demonstrating:
- Basic video conversion
- Custom output paths
- Different language videos
- Batch processing workflows
- Python module integration

### Documentation

#### `VIDEO_CONVERTER_README.md` (Complete Documentation)
Comprehensive documentation including:
- Features overview
- Installation instructions
- Usage examples for all scenarios
- Supported languages
- Output format details
- How it works (technical details)
- Limitations and troubleshooting
- Advanced usage and Python API
- Performance tips

#### `QUICKSTART.md` (Quick Start Guide)
Fast-track guide for getting started:
- Quick installation steps
- Basic usage examples
- Common issues and solutions
- Quick reference table

#### `PROJECT_STRUCTURE.md` (This File)
Project organization and file descriptions.

### Configuration

#### `requirements.txt`
Python dependencies:
- moviepy==1.0.3 (video processing)
- SpeechRecognition==3.14.3 (speech-to-text)
- python-docx==1.2.0 (DOCX generation)
- pydub==0.25.1 (audio processing)

## Architecture

### Component Flow

```
Video File (.mp4, .avi, etc.)
    ↓
[1] Audio Extraction (MoviePy)
    ↓
Audio File (.wav)
    ↓
[2] Speech Recognition (Google API)
    ↓
Text Transcription
    ↓
[3] Document Generation (python-docx)
    ↓
DOCX File (transcript.docx)
```

### Core Components

#### 1. VideoToTextConverter Class
Main converter class with methods:
- `extract_audio()` - Extract audio from video using MoviePy
- `transcribe_audio()` - Convert audio to text using SpeechRecognition
- `create_docx()` - Generate formatted DOCX document
- `convert()` - Main workflow orchestrator

#### 2. Audio Processing
- Extracts audio track from video
- Converts to WAV format (mono, 16-bit PCM)
- Creates temporary files (auto-cleaned)
- Handles videos without audio tracks

#### 3. Speech Recognition
- Uses Google Speech Recognition API
- Processes audio in 30-second chunks
- Supports multiple languages
- Handles recognition errors gracefully
- Combines chunks into coherent text

#### 4. Document Generation
- Creates professional DOCX documents
- Includes metadata (source, date, language)
- Formatted paragraphs with proper spacing
- Custom fonts and styling
- Footer attribution

## Features

### Supported Video Formats
- MP4, AVI, MOV, MKV, WMV, FLV
- Any format supported by FFmpeg

### Supported Languages
Over 100 languages including:
- English (en-US, en-GB)
- Spanish (es-ES)
- French (fr-FR)
- German (de-DE)
- Italian (it-IT)
- Portuguese (pt-BR)
- Japanese (ja-JP)
- Korean (ko-KR)
- Chinese (zh-CN)
- And many more...

### Output Features
- Professional DOCX format
- Metadata inclusion
- Paragraph formatting
- Custom fonts (Calibri, 11pt)
- Centered titles
- Footer attribution

## System Requirements

### Software
- Python 3.9 or higher
- FFmpeg (bundled with moviepy)
- Internet connection (for speech recognition)

### Python Packages
See `requirements.txt` for full list

### Operating System
- Linux (tested on Amazon Linux 2023)
- macOS
- Windows

## Usage Scenarios

### 1. Meeting Transcriptions
Convert recorded video meetings into searchable text documents.

### 2. Lecture Notes
Transcribe educational videos for study materials.

### 3. Interview Documentation
Create text records of video interviews.

### 4. Content Analysis
Extract spoken content from videos for analysis.

### 5. Accessibility
Make video content accessible in text format.

### 6. Subtitle Base
Generate base text for subtitle creation.

## Performance

### Processing Time
- ~1-2 minutes per 30 seconds of video
- Depends on audio quality and internet speed
- Longer videos take proportionally longer

### Resource Usage
- Moderate CPU usage during audio extraction
- Minimal during transcription (API-based)
- Temporary disk space for audio files
- Network bandwidth for API calls

## Limitations

- Requires internet connection for transcription
- Accuracy depends on audio quality
- Background noise affects results
- Google Speech Recognition API has free tier limits
- Very long videos require patience

## Future Enhancements

Possible improvements:
- Offline transcription options
- Additional speech recognition engines
- Timestamp integration
- Speaker identification
- Enhanced text formatting
- Custom DOCX styling options
- Progress bars for long videos
- GPU acceleration for audio processing

## Development

### Testing
Test the main script:
```bash
python3 video_to_text.py --help
```

Test the batch converter:
```bash
python3 batch_convert.py --help
```

### Integration
Use as a Python module:
```python
from video_to_text import VideoToTextConverter

converter = VideoToTextConverter('video.mp4')
output = converter.convert()
```

## Support

For issues or questions:
1. Check `VIDEO_CONVERTER_README.md` for detailed documentation
2. Review `QUICKSTART.md` for common issues
3. Verify all dependencies are installed
4. Check internet connection for API access

## License

This project is provided as-is for educational and commercial use.

---

**Project Status:** Production Ready

**Version:** 1.0.0

**Last Updated:** 2025-11-06

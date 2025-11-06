# Video to Text Converter

A powerful Python-based agent that converts any video file into a text transcription and saves it as a professionally formatted DOCX document.

## Features

- Extracts audio from any video format (MP4, AVI, MOV, MKV, WMV, FLV, etc.)
- Transcribes speech to text using Google Speech Recognition API
- Supports multiple languages
- Generates professional DOCX documents with:
  - Title and metadata (source video, date, language)
  - Formatted transcription text
  - Proper paragraph structure
- Handles long videos by processing audio in chunks
- Automatic cleanup of temporary files
- Command-line interface for easy use

## Requirements

- Python 3.9 or higher
- Internet connection (for Google Speech Recognition API)
- FFmpeg (usually bundled with moviepy)

## Installation

1. Install Python dependencies:

```bash
python3 -m pip install --user -r requirements.txt
```

Or install packages individually:

```bash
python3 -m pip install --user moviepy SpeechRecognition python-docx pydub
```

2. Make the script executable (optional):

```bash
chmod +x video_to_text.py
```

## Usage

### Basic Usage

Convert a video to text (output will be saved as `video.docx`):

```bash
python3 video_to_text.py video.mp4
```

### Specify Output File

```bash
python3 video_to_text.py video.mp4 -o transcript.docx
```

### Specify Language

For Spanish:
```bash
python3 video_to_text.py video.mp4 -l es-ES
```

For French:
```bash
python3 video_to_text.py video.mp4 -l fr-FR
```

For German:
```bash
python3 video_to_text.py video.mp4 -l de-DE
```

### Full Example

```bash
python3 video_to_text.py meeting.mp4 -o meeting_notes.docx -l en-US
```

## Command-Line Arguments

| Argument | Description | Required | Default |
|----------|-------------|----------|---------|
| `video` | Path to the video file | Yes | - |
| `-o, --output` | Output DOCX file path | No | Same name as video with .docx |
| `-l, --language` | Language code for speech recognition | No | en-US |

## Supported Languages

Common language codes:
- `en-US` - English (United States)
- `en-GB` - English (United Kingdom)
- `es-ES` - Spanish (Spain)
- `fr-FR` - French (France)
- `de-DE` - German (Germany)
- `it-IT` - Italian (Italy)
- `pt-BR` - Portuguese (Brazil)
- `ja-JP` - Japanese
- `ko-KR` - Korean
- `zh-CN` - Chinese (Simplified)

See [Google Cloud Speech-to-Text documentation](https://cloud.google.com/speech-to-text/docs/languages) for complete list.

## Output Format

The generated DOCX file includes:

1. **Title Section**: "Video Transcription"
2. **Metadata**:
   - Source video filename
   - Transcription date and time
   - Language used
3. **Transcription Text**: Formatted and paragraph-separated text
4. **Footer**: Generator attribution

## How It Works

1. **Audio Extraction**: Extracts audio from the video file using MoviePy
2. **Audio Processing**: Converts audio to WAV format (mono channel, 16-bit PCM)
3. **Speech Recognition**: Processes audio in 30-second chunks using Google Speech Recognition API
4. **Text Assembly**: Combines all transcribed chunks into coherent text
5. **Document Generation**: Creates a formatted DOCX document with the transcription
6. **Cleanup**: Removes temporary audio files

## Limitations

- Requires internet connection for speech recognition
- Accuracy depends on:
  - Audio quality in the video
  - Background noise levels
  - Speaker clarity and accent
  - Language complexity
- Google Speech Recognition has usage limits for free tier
- Very long videos may take considerable time to process

## Troubleshooting

### No audio detected
- Ensure your video file has an audio track
- Check that the audio isn't muted or corrupted

### Poor transcription quality
- Try improving the video's audio quality
- Use videos with clear speech and minimal background noise
- Specify the correct language code with `-l`

### Connection errors
- Check your internet connection
- Google's Speech Recognition API may be temporarily unavailable

### FFmpeg errors
- Ensure FFmpeg is properly installed
- On Linux: `sudo dnf install ffmpeg` (Amazon Linux 2023)
- On Ubuntu/Debian: `sudo apt-get install ffmpeg`
- On macOS: `brew install ffmpeg`

## Example Use Cases

1. **Meeting Transcriptions**: Convert recorded video meetings into text documents
2. **Lecture Notes**: Transcribe educational videos for study materials
3. **Interview Documentation**: Create text records of video interviews
4. **Subtitle Creation**: Generate base text for subtitle creation
5. **Content Accessibility**: Make video content accessible in text format
6. **Video Analysis**: Extract and analyze spoken content from videos

## Advanced Usage

### Using as a Python Module

```python
from video_to_text import VideoToTextConverter

# Create converter instance
converter = VideoToTextConverter(
    video_path='presentation.mp4',
    output_path='presentation_transcript.docx',
    language='en-US'
)

# Run conversion
output_file = converter.convert()
print(f"Transcription saved to: {output_file}")
```

### Batch Processing Multiple Videos

```python
import os
from pathlib import Path
from video_to_text import VideoToTextConverter

video_folder = Path('videos')
output_folder = Path('transcripts')
output_folder.mkdir(exist_ok=True)

for video_file in video_folder.glob('*.mp4'):
    print(f"\nProcessing: {video_file.name}")
    output_path = output_folder / f"{video_file.stem}_transcript.docx"

    try:
        converter = VideoToTextConverter(
            video_path=str(video_file),
            output_path=str(output_path),
            language='en-US'
        )
        converter.convert()
    except Exception as e:
        print(f"Error processing {video_file.name}: {e}")
```

## Performance Tips

1. For better accuracy:
   - Use high-quality video files with clear audio
   - Minimize background noise
   - Ensure speakers face the microphone/camera

2. For faster processing:
   - Use shorter video clips when possible
   - Close other applications to free up system resources

3. For long videos:
   - Be patient - processing time increases with video length
   - Consider splitting very long videos into smaller segments

## Contributing

Feel free to enhance this tool with:
- Additional speech recognition engines
- Offline transcription options
- Enhanced text formatting
- Timestamp integration
- Speaker identification
- Custom DOCX styling options

## License

This project is provided as-is for educational and commercial use.

## Support

For issues, questions, or feature requests, please create an issue in the project repository.

---

**Generated by Video to Text Converter Agent**

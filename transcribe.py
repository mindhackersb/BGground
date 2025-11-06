#!/usr/bin/env python3
"""
CLI tool to transcribe any video or audio file to text and export as DOCX.
"""

import argparse
import os
import sys
import tempfile
from pathlib import Path

import docx
import ffmpeg
import whisper
from moviepy.editor import VideoFileClip
from pydub import AudioSegment


def ensure_audio(input_path: Path) -> Path:
    """Ensure we have a pure audio file (wav) from any input."""
    suffix = input_path.suffix.lower()
    if suffix in {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg"}:
        return input_path

    # Extract audio from video via moviepy
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        audio_path = Path(tmp.name)

    clip = VideoFileClip(str(input_path))
    clip.audio.write_audiofile(str(audio_path), verbose=False, logger=None)
    clip.close()
    return audio_path


def normalise_audio(input_path: Path) -> Path:
    """Convert any audio file to 16kHz mono WAV for Whisper."""
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(16000).set_channels(1)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        output_path = Path(tmp.name)
    audio.export(output_path, format="wav")
    return output_path


def transcribe_audio(audio_path: Path, model_size: str) -> str:
    model = whisper.load_model(model_size)
    result = model.transcribe(str(audio_path))
    return result["text"].strip()


def save_to_docx(text: str, output_path: Path) -> None:
    document = docx.Document()
    for paragraph in text.split("\n\n"):
        document.add_paragraph(paragraph)
    document.save(str(output_path))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to input video/audio file")
    parser.add_argument("--model", default="base", help="Whisper model size (tiny, base, small, medium, large)")
    parser.add_argument("--output", type=Path, help="Output DOCX path", default=None)
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Input file {args.input} does not exist", file=sys.stderr)
        sys.exit(1)

    audio_source = ensure_audio(args.input)
    normalised_audio = normalise_audio(audio_source)

    try:
        text = transcribe_audio(normalised_audio, args.model)
    finally:
        if audio_source != args.input and audio_source.exists():
            audio_source.unlink()
        if normalised_audio.exists():
            normalised_audio.unlink()

    output_path = args.output or args.input.with_suffix(".docx")
    save_to_docx(text, output_path)
    print(f"Transcription saved to {output_path}")


if __name__ == "__main__":
    main()

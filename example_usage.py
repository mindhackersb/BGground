#!/usr/bin/env python3
"""
Example usage script for Video to Text Converter
"""

from video_to_text import VideoToTextConverter
from pathlib import Path


def example_basic_conversion():
    """Example 1: Basic video to text conversion"""
    print("\n=== Example 1: Basic Conversion ===")

    try:
        converter = VideoToTextConverter(
            video_path='sample_video.mp4'
        )
        output_file = converter.convert()
        print(f"\nSuccess! Transcription saved to: {output_file}")

    except FileNotFoundError:
        print("Error: sample_video.mp4 not found. Please provide a valid video file.")
    except Exception as e:
        print(f"Error: {e}")


def example_custom_output():
    """Example 2: Custom output path"""
    print("\n=== Example 2: Custom Output Path ===")

    try:
        converter = VideoToTextConverter(
            video_path='interview.mp4',
            output_path='interview_transcript.docx'
        )
        output_file = converter.convert()
        print(f"\nSuccess! Transcription saved to: {output_file}")

    except FileNotFoundError:
        print("Error: interview.mp4 not found. Please provide a valid video file.")
    except Exception as e:
        print(f"Error: {e}")


def example_different_language():
    """Example 3: Spanish language video"""
    print("\n=== Example 3: Spanish Language Video ===")

    try:
        converter = VideoToTextConverter(
            video_path='video_espanol.mp4',
            output_path='transcripcion.docx',
            language='es-ES'
        )
        output_file = converter.convert()
        print(f"\nSuccess! Transcription saved to: {output_file}")

    except FileNotFoundError:
        print("Error: video_espanol.mp4 not found. Please provide a valid video file.")
    except Exception as e:
        print(f"Error: {e}")


def example_batch_processing():
    """Example 4: Batch process multiple videos"""
    print("\n=== Example 4: Batch Processing ===")

    # List of videos to process
    videos = ['video1.mp4', 'video2.mp4', 'video3.mp4']

    # Create output directory
    output_dir = Path('transcripts')
    output_dir.mkdir(exist_ok=True)

    for video_path in videos:
        if not Path(video_path).exists():
            print(f"Skipping {video_path} - file not found")
            continue

        try:
            output_path = output_dir / f"{Path(video_path).stem}_transcript.docx"

            print(f"\n{'='*60}")
            print(f"Processing: {video_path}")
            print('='*60)

            converter = VideoToTextConverter(
                video_path=video_path,
                output_path=str(output_path)
            )
            converter.convert()

        except Exception as e:
            print(f"Error processing {video_path}: {e}")
            continue


if __name__ == '__main__':
    print("Video to Text Converter - Example Usage")
    print("=" * 60)

    # Uncomment the examples you want to run:

    # example_basic_conversion()
    # example_custom_output()
    # example_different_language()
    # example_batch_processing()

    print("\n\nNote: Make sure to provide actual video files and uncomment")
    print("the examples you want to run in this script.")

#!/usr/bin/env python3
"""
Batch Video to Text Converter
Process multiple video files at once
"""

import os
import sys
import argparse
from pathlib import Path
from video_to_text import VideoToTextConverter


def batch_convert(input_dir, output_dir=None, pattern='*.mp4', language='en-US', recursive=False):
    """
    Convert all video files in a directory to text documents.

    Args:
        input_dir (str): Directory containing video files
        output_dir (str): Directory for output DOCX files (default: same as input)
        pattern (str): File pattern to match (default: *.mp4)
        language (str): Language code for speech recognition
        recursive (bool): Search subdirectories recursively
    """
    input_path = Path(input_dir)

    if not input_path.exists():
        print(f"Error: Input directory not found: {input_dir}")
        return 1

    if not input_path.is_dir():
        print(f"Error: Not a directory: {input_dir}")
        return 1

    # Set output directory
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = input_path

    # Find video files
    if recursive:
        video_files = list(input_path.rglob(pattern))
    else:
        video_files = list(input_path.glob(pattern))

    if not video_files:
        print(f"No video files found matching pattern: {pattern}")
        return 1

    print(f"\nFound {len(video_files)} video file(s) to process")
    print("=" * 60)

    # Process each video
    successful = 0
    failed = 0
    failed_files = []

    for i, video_file in enumerate(video_files, 1):
        print(f"\n[{i}/{len(video_files)}] Processing: {video_file.name}")
        print("-" * 60)

        try:
            # Generate output filename
            if output_dir:
                output_file = output_path / f"{video_file.stem}_transcript.docx"
            else:
                output_file = video_file.with_suffix('.docx')

            # Check if output already exists
            if output_file.exists():
                response = input(f"Output file already exists: {output_file.name}\n"
                               f"Overwrite? (y/n): ")
                if response.lower() != 'y':
                    print("Skipped.")
                    continue

            # Convert video
            converter = VideoToTextConverter(
                video_path=str(video_file),
                output_path=str(output_file),
                language=language
            )
            converter.convert()

            successful += 1
            print(f"\nSuccess! Output saved to: {output_file}")

        except Exception as e:
            failed += 1
            failed_files.append((video_file.name, str(e)))
            print(f"\nError processing {video_file.name}: {e}")
            continue

    # Print summary
    print("\n" + "=" * 60)
    print("BATCH CONVERSION SUMMARY")
    print("=" * 60)
    print(f"Total files: {len(video_files)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

    if failed_files:
        print("\nFailed files:")
        for filename, error in failed_files:
            print(f"  - {filename}: {error}")

    print("\nBatch processing completed.")
    return 0 if failed == 0 else 1


def main():
    """Command-line interface for batch conversion."""
    parser = argparse.ArgumentParser(
        description='Batch convert video files to text documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python batch_convert.py videos/
  python batch_convert.py videos/ -o transcripts/
  python batch_convert.py videos/ -p "*.avi" -r
  python batch_convert.py videos/ -o output/ -l es-ES
        """
    )

    parser.add_argument(
        'input_dir',
        help='Directory containing video files'
    )

    parser.add_argument(
        '-o', '--output',
        help='Output directory for DOCX files (default: same as input)',
        default=None
    )

    parser.add_argument(
        '-p', '--pattern',
        help='File pattern to match (default: *.mp4)',
        default='*.mp4'
    )

    parser.add_argument(
        '-l', '--language',
        help='Language code for speech recognition (default: en-US)',
        default='en-US'
    )

    parser.add_argument(
        '-r', '--recursive',
        help='Search subdirectories recursively',
        action='store_true'
    )

    args = parser.parse_args()

    try:
        return batch_convert(
            input_dir=args.input_dir,
            output_dir=args.output,
            pattern=args.pattern,
            language=args.language,
            recursive=args.recursive
        )
    except KeyboardInterrupt:
        print("\n\nBatch conversion interrupted by user.")
        return 130
    except Exception as e:
        print(f"\nFatal error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())

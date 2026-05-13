"""Command-line interface for podcast RSS generator."""

import argparse
import sys
from pathlib import Path

from .generator import generate_rss_feed


def main(argv=None):
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="podcast-rss-generator",
        description="Convert podcast metadata from YAML to RSS 2.0 feeds compatible with Apple Podcasts and Spotify.",
    )
    
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        default="feed.yaml",
        help="Path to YAML podcast configuration file (default: feed.yaml)"
    )
    
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default="podcast.xml",
        help="Path where RSS feed will be written (default: podcast.xml)"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )
    
    args = parser.parse_args(argv)
    
    try:
        output_path = generate_rss_feed(args.input, args.output)
        print(f"✅ RSS feed generated successfully: {output_path}")
        return 0
    except FileNotFoundError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"❌ Invalid configuration: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

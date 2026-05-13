"""Tests for podcast RSS generator."""

import tempfile
from pathlib import Path

from podcast_rss_generator import generate_rss_feed


def test_generate_rss_feed_basic():
    """Test basic RSS feed generation."""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a minimal YAML config
        yaml_content = """
title: Test Podcast
subtitle: A test podcast
author: Test Author
description: This is a test podcast
link: https://example.com
image: /images/artwork.jpg
language: en-us
category: Technology
format: audio/mpeg
item:
  - title: "Episode 1"
    description: "Test episode"
    published: "Thu, 12 Jan 2023 18:00:00 GMT"
    file: /audio/ep1.mp3
    duration: "00:30:00"
    length: 36000000
"""
        
        yaml_path = tmpdir / "feed.yaml"
        output_path = tmpdir / "podcast.xml"
        
        yaml_path.write_text(yaml_content)
        
        # Generate feed
        result = generate_rss_feed(yaml_path, output_path)
        
        assert result.exists()
        assert result.name == "podcast.xml"
        
        # Verify content
        content = result.read_text()
        assert "Test Podcast" in content
        assert "Test Author" in content
        assert "Episode 1" in content
        assert "rss version" in content


if __name__ == "__main__":
    test_generate_rss_feed_basic()
    print("✅ Test passed!")

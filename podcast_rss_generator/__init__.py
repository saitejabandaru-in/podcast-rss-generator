"""Podcast RSS Generator - Convert YAML podcast configs to RSS 2.0 feeds."""

__version__ = "1.0.0"
__author__ = "Sai Teja Bandaru"
__license__ = "MIT"

from .generator import generate_rss_feed

__all__ = ["generate_rss_feed"]

#!/usr/bin/env python
"""Setup configuration for podcast-rss-generator package."""

from setuptools import setup, find_packages

setup(
    name="podcast-rss-generator",
    version="1.0.0",
    author="Sai Teja Bandaru",
    author_email="contact@saitejabandaru.com",
    description="Convert podcast metadata from YAML to RSS 2.0 feeds compatible with Apple Podcasts, Spotify, and major podcast platforms.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/saitejabandaru-in/podcast-test",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pyyaml>=5.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries",
    ],
    entry_points={
        "console_scripts": [
            "podcast-rss-generator=podcast_rss_generator.cli:main",
        ],
    },
)

"""Core podcast RSS feed generation module."""

import xml.etree.ElementTree as xml_tree
from pathlib import Path
from typing import Union, Dict, Any

import yaml


def generate_rss_feed(
    yaml_path: Union[str, Path],
    output_path: Union[str, Path] = "podcast.xml"
) -> Path:
    """
    Generate an RSS 2.0 feed from a YAML podcast configuration.
    
    Args:
        yaml_path: Path to the YAML configuration file
        output_path: Path where the RSS feed will be written (default: podcast.xml)
    
    Returns:
        Path to the generated RSS feed file
    
    Raises:
        FileNotFoundError: If the YAML file does not exist
        ValueError: If the YAML structure is invalid
    """
    yaml_path = Path(yaml_path)
    output_path = Path(output_path)
    
    if not yaml_path.exists():
        raise FileNotFoundError(f"YAML file not found: {yaml_path}")
    
    # Load YAML configuration
    with open(yaml_path, 'r', encoding='utf-8') as file:
        yaml_data = yaml.safe_load(file)
    
    if not yaml_data:
        raise ValueError("YAML file is empty or invalid")
    
    # Create RSS structure
    rss_element = xml_tree.Element('rss', {
        'version': '2.0',
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
    })
    
    channel_element = xml_tree.SubElement(rss_element, 'channel')
    link_prefix = yaml_data.get('link', '')
    
    # Add channel metadata
    _add_channel_metadata(channel_element, yaml_data, link_prefix)
    
    # Process episodes
    items = yaml_data.get('item', [])
    for episode in items:
        _add_episode(channel_element, episode, yaml_data, link_prefix)
    
    # Write output
    output_tree = xml_tree.ElementTree(rss_element)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_tree.write(str(output_path), encoding='UTF-8', xml_declaration=True)
    
    return output_path


def _add_channel_metadata(channel: xml_tree.Element, data: Dict[str, Any], link_prefix: str) -> None:
    """Add channel-level metadata to the RSS feed."""
    if 'title' in data:
        xml_tree.SubElement(channel, 'title').text = data['title']
    
    if 'author' in data:
        xml_tree.SubElement(channel, 'itunes:author').text = data['author']
    
    if 'language' in data:
        xml_tree.SubElement(channel, 'language').text = data['language']
    
    if 'image' in data:
        xml_tree.SubElement(channel, 'itunes:image', {
            'href': link_prefix + data['image']
        })
    
    if 'subtitle' in data:
        xml_tree.SubElement(channel, 'subtitle').text = data['subtitle']
    
    if 'description' in data:
        xml_tree.SubElement(channel, 'description').text = data['description']
    
    if 'format' in data:
        xml_tree.SubElement(channel, 'format').text = data['format']
    
    if link_prefix:
        xml_tree.SubElement(channel, 'link').text = link_prefix
    
    if 'category' in data:
        xml_tree.SubElement(channel, 'itunes:category', {
            'text': data['category']
        })


def _add_episode(
    channel: xml_tree.Element,
    episode: Dict[str, Any],
    podcast_data: Dict[str, Any],
    link_prefix: str
) -> None:
    """Add an episode (item) to the RSS feed."""
    item_element = xml_tree.SubElement(channel, 'item')
    
    if 'title' in episode:
        xml_tree.SubElement(item_element, 'title').text = episode['title']
    
    if 'author' in podcast_data:
        xml_tree.SubElement(item_element, 'itunes:author').text = podcast_data['author']
    
    if 'description' in episode:
        xml_tree.SubElement(item_element, 'description').text = episode['description']
    
    if 'duration' in episode:
        xml_tree.SubElement(item_element, 'itunes:duration').text = episode['duration']
    
    if 'published' in episode:
        xml_tree.SubElement(item_element, 'pubDate').text = episode['published']
    
    # Add audio file enclosure
    if 'file' in episode and 'length' in episode:
        xml_tree.SubElement(item_element, 'enclosure', {
            'url': link_prefix + episode['file'],
            'type': 'audio/mpeg',
            'length': str(episode['length'])
        })

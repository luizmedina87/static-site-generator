import re

from textnode import TextType, TextNode


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    split_nodes = []
    for node in old_nodes:
        starts_with_delimiter = node.text.find(delimiter) == 0
        first_type = text_type if starts_with_delimiter else TextType.TEXT
        second_type = text_type if not starts_with_delimiter else TextType.TEXT
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 == 1:
            raise Exception(f"Invalid Markdown syntax. Odd number of '{delimiter}'s.")
        split_nodes = node.text.split(delimiter)
        split_nodes = [s for s in split_nodes if s]
        for index, split_node in enumerate(split_nodes):
            fragment_type = first_type if index % 2 == 0 else second_type
            split_nodes[index] = TextNode(split_node, fragment_type)
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text:str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        raise Exception("No nodes given.")
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        image_nodes = extract_markdown_images(old_node.text)
        if not image_nodes:
            new_nodes.append(old_node)
            continue
        text_to_split = old_node.text
        for image_node in image_nodes:
            image_text, image_url = image_node
            split_sequence = f"![{image_text}]({image_url})"
            split_text = text_to_split.split(split_sequence, 1)
            text_to_split = split_text[1]
            text_node = TextNode(split_text[0], TextType.TEXT)
            image_node = TextNode(image_text, TextType.IMAGE, image_url)
            if split_text[0]:
                new_nodes.append(text_node)
            new_nodes.append(image_node)
        if split_text[1]:
            text_node = TextNode(split_text[1], TextType.TEXT)
            new_nodes.append(text_node)
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        raise Exception("No nodes given.")
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        link_nodes = extract_markdown_links(old_node.text)
        if not link_nodes:
            new_nodes.append(old_node)
            continue
        text_to_split = old_node.text
        for link_node in link_nodes:
            link_text, link_url = link_node
            split_sequence = f"[{link_text}]({link_url})"
            split_text = text_to_split.split(split_sequence, 1)
            text_to_split = split_text[1]
            text_node = TextNode(split_text[0], TextType.TEXT)
            link_node = TextNode(link_text, TextType.LINK, link_url)
            if split_text[0]:
                new_nodes.append(text_node)
            new_nodes.append(link_node)
        if split_text[1]:
            text_node = TextNode(split_text[1], TextType.TEXT)
            new_nodes.append(text_node)
    return new_nodes
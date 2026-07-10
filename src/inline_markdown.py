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
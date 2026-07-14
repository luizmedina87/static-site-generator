def markdown_to_blocks(markdown: str) -> list[str]:
    dirty_blocks = markdown.split("\n\n")
    clean_blocks = []
    for block in dirty_blocks:
        if not block:
            continue
        clean_blocks.append(block.strip())
    return clean_blocks
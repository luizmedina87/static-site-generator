import os

from markdown_blocks import markdown_to_html_node
from inline_markdown import extract_title


TITLE_PATTERN = "{{ Title }}"
CONTENT_PATTERN = "{{ Content }}"


def generate_page(
        from_path: str, 
        template_path: str, 
        dest_path: str,
        basepath: str
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as from_file:
        from_content = from_file.read()
    with open(template_path, "r") as template_file:
        template_content = template_file.read()
    if not from_content:
        raise Exception(f"{from_path} is empty")
    if not template_file:
        raise Exception(f"{template_file} is empty")
    
    html_title = extract_title(from_content)
    html_tree = markdown_to_html_node(from_content)
    html_string = html_tree.to_html()
    dest_content = (
        template_content.replace(TITLE_PATTERN, html_title)
                        .replace(CONTENT_PATTERN, html_string)
                        .replace('''href="/''', f'''href="{basepath}''')
                        .replace('''src="/''', f'''src="{basepath}''')
    )
    
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok="True")

    with open(dest_path, "w") as dest_file:
        dest_file.write(dest_content)


def generate_pages_recursive(
        dir_path_content: str,
        template_path: str,
        dest_dir_path: str,
        basepath: str
) -> None:
    contents = os.listdir(dir_path_content)
    for content in contents:
        content_path = os.path.join(dir_path_content, content)
        if os.path.isfile(content_path):
            dest_dir_file_path = os.path.join(dest_dir_path, "index.html")
            generate_page(
                content_path,
                template_path,
                dest_dir_file_path,
                basepath
            )
        else:
            recursive_dest_path = os.path.join(dest_dir_path, content)
            generate_pages_recursive(
                content_path, 
                template_path, 
                recursive_dest_path,
                basepath
            )

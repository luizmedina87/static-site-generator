from copystatic import replace_static_public
from generate_page import generate_pages_recursive
from constants import (
    TEMPLATE_HTML,
    CONTENT_DIR,
    PUBLIC_DIR,
)


def main():
    replace_static_public()
    generate_pages_recursive(CONTENT_DIR, TEMPLATE_HTML, PUBLIC_DIR)


main()
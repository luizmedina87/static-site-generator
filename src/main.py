import sys

from copystatic import replace_static_docs
from generate_page import generate_pages_recursive
from constants import (
    TEMPLATE_HTML,
    CONTENT_DIR,
    PUBLIC_DIR,
)


def main():
    if len(sys.argv) < 2:
        print("please provide the base path")
        sys.exit(1)
    basepath = sys.argv[1]
    replace_static_docs()
    generate_pages_recursive(CONTENT_DIR, TEMPLATE_HTML, PUBLIC_DIR, basepath)


main()
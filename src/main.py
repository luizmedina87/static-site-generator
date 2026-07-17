import os

from copystatic import replace_static_public
from generate_page import generate_page
from constants import (
    INDEX_MD,
    TEMPLATE_HTML,
    INDEX_HTML,
)


def main():
    replace_static_public()
    generate_page(INDEX_MD, TEMPLATE_HTML, INDEX_HTML)


main()
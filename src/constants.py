import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
STATIC_DIR = os.path.join(ROOT_DIR, "static")
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
CONTENT_DIR = os.path.join(ROOT_DIR, "content")
INDEX_MD = os.path.join(CONTENT_DIR, "index.md")
TEMPLATE_HTML = os.path.join(ROOT_DIR, "template.html")
INDEX_HTML = os.path.join(PUBLIC_DIR, "index.html")
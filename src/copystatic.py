import os
import shutil

from textnode import TextNode

from copystatic import replace_static_public


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
STATIC_DIR = os.path.join(ROOT_DIR, "static")
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")


def replace_static_public():
    if not os.path.exists(STATIC_DIR):
        raise Exception(f"{STATIC_DIR} not found")
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
        print(f"{PUBLIC_DIR} removed")
    os.mkdir(PUBLIC_DIR)
    print(f"{PUBLIC_DIR} created")
    copy_contents(STATIC_DIR, PUBLIC_DIR)


def copy_contents(src, dst):
    contents = os.listdir(src)
    for content in contents:
        src_content = os.path.join(src, content)
        if os.path.isfile(src_content):
            shutil.copy(src_content, dst)
            print(f"{content} copied")
        else:
            os.mkdir(os.path.join(dst, content))
            print(f"{content}/ created")
            copy_contents(src_content, os.path.join(dst, content))

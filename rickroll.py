#!/usr/bin/env python3

# Usage:
#   rickroll.py [FILES]

from os import path
from re import sub
from sys import argv

RICKROLL_LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def transform_markdown(s):
    return sub(r"\[([^]]+)\]\([^)]+\)", rf"[\1]({RICKROLL_LINK})", s);

def transform_html(s):
    return sub(r"(<a [^>]*href=[\"'])[^\"']+([\"'][^>]*>[^>]+</a>)", rf"\1{RICKROLL_LINK}\2", s);

def transform_file(file_path):
    extension = path.splitext(file_path)[1]

    with open(file_path, "r+") as f:
        s = f.read();
        f.seek(0);

        if extension == ".md":
            f.write(transform_markdown(s));
        elif extension == ".html":
            f.write(transform_html(s));
        else:
            assert False, "not implemented";

        f.truncate();

if __name__ == "__main__":
    for arg in argv[1:]:
        print(f"File: {arg}");
        transform_file(arg);

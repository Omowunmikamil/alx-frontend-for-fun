#!/usr/bin/python3
"""
This script converts a markdown file to HTML. It takes a argument(a string i.e. the markdown file)
    Usage: 
        Usage: ./markdown2html.py README.md README.html
"""

from sys import argv
import sys
import os


if __name__ == "__main__":

    if len(argv) != 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    markdown_file = argv[1]

    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)
    
    sys.exit(0)

import argparse
import sys

import mistletoe


def extract_headers(file_path):
    with open(file_path, "r") as file:
        markdown_content = file.read()

    parsed_markdown = mistletoe.Document(markdown_content)
    headers = []

    def _traverse(node):
        if isinstance(node, mistletoe.block_token.Heading):
            headers.append(node.children[0].content)
        for child in getattr(node, "children", []):
            _traverse(child)

    _traverse(parsed_markdown)
    return headers


def add_section(file_path, section_name):
    with open(file_path, "r") as file:
        markdown_content = file.read()

    if section_name not in markdown_content:
        markdown_content += f"\n## [[{section_name}]]\n- [x] shopping\n"

    with open(file_path, "w") as file:
        file.write(markdown_content)


def main():
    parser = argparse.ArgumentParser(description="Add sections to markdown files.")
    parser.add_argument(
        "stores", metavar="store", type=str, nargs="+", help="stores to add as sections"
    )
    args = parser.parse_args()

    file_paths = [line.strip() for line in sys.stdin]

    for file_path in file_paths:
        existing_headers = extract_headers(file_path)
        for store in args.stores:
            if store not in existing_headers:
                add_section(file_path, store)

    print("Sections added successfully.")


if __name__ == "__main__":
    main()

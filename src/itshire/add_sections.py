import logging
import sys

import mistletoe


def extract_headers(file_path):
    with open(file_path, "r") as file:
        markdown_content = file.read()

    parsed_markdown = mistletoe.Document(markdown_content)
    headers = []

    def _traverse(node):
        if isinstance(node, mistletoe.block_token.Heading):
            logging.debug(parsed_markdown)
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
    file_paths = [line.strip() for line in sys.stdin if line.strip()]

    stores = [
        "Central Co-op",
        "Hau Hau Market",
        "M2M",
        "PCC",
        "Safeway",
        "Trader Joes",
        "Uwajimaya",
    ]

    for file_path in file_paths:
        logging.info(f"file path: {file_path}")
        if not file_path.startswith("/"):
            print(f"Skipping invalid file path: {file_path}")
            continue

        existing_headers = extract_headers(file_path)
        for store_name in stores:
            if store_name not in existing_headers:
                add_section(file_path, store_name)

    print("Sections added successfully.")


if __name__ == "__main__":
    main()

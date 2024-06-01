import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Add sections to markdown files.")
    parser.add_argument(
        "stores", metavar="store", type=str, nargs="+", help="stores to add as sections"
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    args = parser.parse_args()
    return args

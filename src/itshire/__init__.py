import logging

from . import cli
from . import log as logmod

__project_name__ = "itshire"


def main() -> int:
    args = cli.parse_args()
    logmod.configure_logging(args.verbose)
    logging.debug("test")
    print("hello")
    return 0

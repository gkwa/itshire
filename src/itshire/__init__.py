from . import add_sections, cli
from . import log as logmod

__project_name__ = "itshire"


def main() -> int:
    args = cli.parse_args()
    logmod.configure_logging(args.verbose)

    if args.command == "addstores":
        add_sections.main()
    else:
        print("hello")

    return 0

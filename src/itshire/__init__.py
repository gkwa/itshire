import logging

import itshire.add_sections
import itshire.cli
import itshire.log

__project_name__ = "itshire"


def main() -> int:
    args = itshire.cli.parse_args()
    itshire.log.configure_logging(args.verbose)
    logging.debug("Starting itshire")

    if args.command == "addstores":
        try:
            itshire.add_sections.main(args.directory)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return 1
    else:
        print("Unknown command")
        return 1

    return 0

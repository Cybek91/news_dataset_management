import argparse
import logging
from search_engine import search_engine
import sys
import time


ENABLED_MODULES = {"search_engine": search_engine}
LOGGER = logging.getLogger(__name__)


def parse_args(args):
    parser = argparse.ArgumentParser(description="Application to manage news in the dataset")
    parser.add_argument(
        "module",
        type=str,
        choices=ENABLED_MODULES.keys(),
        help="application module"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    parser.add_argument(
        "module_args",
        help="arguments passed to the selected module",
        nargs=argparse.REMAINDER,
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    logformat = "[%(asctime)s] %(levelname)s: %(message)s (%(name)s)"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.Formatter.converter = time.gmtime


def main(args):
    params = parse_args(args)
    setup_logging(params.loglevel)
    LOGGER.debug("Starting news dataset management with args %s...", params)
    ENABLED_MODULES[params.module].main(params.module_args)


if __name__ == "__main__":
    main(sys.argv[1:])

import argparse
import logging
from project_config import DB
LOGGER = logging.getLogger(__name__)


def parse_args(args):
    parser = argparse.ArgumentParser(description="News Dataset Management | Search module")
    parser.add_argument(
        "-p",
        "--phrase",
        dest="phrase",
        help="search headlines and descriptions by phrase",
        type=str,
        default=False
    )
    return parser.parse_args(args)


def is_phrase_in_headline_or_description(article, phrase):
    return phrase.lower() in article["headline"].lower() or phrase.lower() in article["short_description"].lower()


def present_data(matching_articles, phrase):
    if len(list(matching_articles)) > 0:
        for article in matching_articles:
            print(f'article headline: {article["headline"]}, article description: {article["short_description"]}')
    else:
        print(f"There is no articles including phrase: '{phrase}'")


def main(args):
    args = parse_args(args)
    LOGGER.info("Finding matching articles...")
    phrase = args.phrase
    matching_articles = (article for article in DB['news'] if is_phrase_in_headline_or_description(article, phrase))
    present_data(matching_articles, phrase)

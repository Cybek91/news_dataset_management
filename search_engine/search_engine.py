import argparse
import logging
import os
import json
LOGGER = logging.getLogger(__name__)
SUPPORTED_ARTICLES_KEYS = {'category', 'headline', 'authors', 'link', 'short_description', 'date'}


def parse_args(args):
    parser = argparse.ArgumentParser(description="News Dataset Management | Search module")
    parser.add_argument(
        "dataset",
        help="name of the json file in the dataset folder",
        type=str,
        default=False
    )
    parser.add_argument(
        "-p",
        "--phrase",
        dest="phrase",
        help="search headlines and descriptions by phrase",
        type=str,
        default=False
    )
    return parser.parse_args(args)


def load_dataset(file_path):
    with open(file_path, "r") as file:
        for line in file.readlines():
            yield line


def is_phrase_in_headline_or_description(article, phrase):
    return phrase in article["headline"].lower() or phrase in article["short_description"].lower()


def find_matching_articles(phrase, dataset):
    matching_articles = []
    for line in dataset:
        article = json.loads(line)
        if not SUPPORTED_ARTICLES_KEYS <= set(article):
            LOGGER.error("Dataset doesn't include supported keys")
            exit()
        if is_phrase_in_headline_or_description(article, phrase.lower()):
            matching_articles.append(article)
    return matching_articles


def present_data(matching_articles):
    for article in matching_articles:
        print(f'article headline: {article["headline"]}, article description: {article["short_description"]}')


def main(args):
    LOGGER.info("Starting Search engine...")
    args = parse_args(args)
    filename = args.dataset
    file_path = os.path.join("dataset", filename)

    if not filename.endswith(".json"):
        LOGGER.error("This type of file is not supported...")
        exit()
    elif not os.path.isfile(file_path):
        LOGGER.error("Specified file doesn't exists...")
        exit()

    LOGGER.info("Loading dataset...")
    dataset = load_dataset(file_path)
    LOGGER.info("Finding matching articles...")
    matching_articles = find_matching_articles(args.phrase, dataset)
    LOGGER.info(f'Found {len(matching_articles)} matching phrase {args.phrase}')

    if len(matching_articles) > 0:
        present_data(matching_articles)



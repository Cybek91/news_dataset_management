import argparse
import logging
import os
import json
from project_config import DB
LOGGER = logging.getLogger(__name__)
SUPPORTED_DATASET_KEYS = {'category', 'headline', 'authors', 'link', 'short_description', 'date'}


def parse_args(args):
    parser = argparse.ArgumentParser(description="News Dataset Management | Import module")
    parser.add_argument(
        "dataset",
        help="name of the json file in the dataset folder",
        type=str,
        default=False
    )
    parser.add_argument(
        "-t",
        "--table_name",
        help="name of the DB table where dataset will be stored",
        type=str,
        default="news"
    )
    return parser.parse_args(args)


def db_connection(func):
    def transaction_wrapper(table_name, *args, **kwargs):
        try:
            DB.begin()
            func(DB[table_name], *args, **kwargs)
            DB.commit()
        except:
            DB.rollback()
            LOGGER.error(f"Something went wrong during saving dataset row to DB.")

    transaction_wrapper.__name__ = func.__name__
    transaction_wrapper.__doc__ = func.__doc__

    return transaction_wrapper


def load_dataset(file_path):
    with open(file_path, "r") as file:
        for line in file.readlines():
            yield line


def process_dataset(dataset_file, table_name):
    for row in dataset_file:
        dataset_row = json.loads(row)
        if not SUPPORTED_DATASET_KEYS <= set(dataset_row):
            LOGGER.error(f"Dataset row doesn't include supported keys, dataset_row: {dataset_row}...skipping")
        else:
            save_dataset_to_db(table_name, dataset_row)


@db_connection
def save_dataset_to_db(db_connector, dataset_row):
    db_connector.insert(dict(
        category=dataset_row["category"],
        headline=dataset_row["headline"],
        authors=dataset_row["authors"],
        link=dataset_row["link"],
        short_description=dataset_row["short_description"],
        date=dataset_row["date"]
    ))


def main(args):
    LOGGER.info("Starting import dataset...")
    args = parse_args(args)
    file_path = os.path.join("dataset", args.dataset)

    if not args.dataset.endswith(".json"):
        LOGGER.error("This type of file is not supported...")
        exit()
    elif not os.path.isfile(file_path):
        LOGGER.error("Specified file doesn't exists...")
        exit()

    LOGGER.info("Loading dataset...")
    dataset_file = load_dataset(file_path)
    process_dataset(dataset_file, args.table_name)
    LOGGER.info("Dataset successfully imported")

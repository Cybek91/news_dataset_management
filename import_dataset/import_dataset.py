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
        "--db_table",
        help="table of the DB where dataset will be stored",
        type=str,
        default="news"
    )
    return parser.parse_args(args)


def load_dataset(file_path):
    with open(file_path, "r") as file:
        for line in file.readlines():
            yield line


def save_to_db(dataset_file, table_name):
    for row in dataset_file:
        dataset_row = json.loads(row)
        if not SUPPORTED_DATASET_KEYS <= set(dataset_row):
            LOGGER.error(f"Dataset row doesn't include supported keys, dataset_row: {dataset_row}...skipping")
        else:
            try:
                DB.begin()
                DB[table_name].insert(dict(
                    category=dataset_row["category"],
                    headline=dataset_row["headline"],
                    authors=dataset_row["authors"],
                    link=dataset_row["link"],
                    short_description=dataset_row["short_description"],
                    date=dataset_row["date"]
                ))
                DB.commit()
            except:
                DB.rollback()
                LOGGER.error(f"Something went wrong during saving dataset row to DB. Dataset row: {dataset_row}")


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
    save_to_db(dataset_file, args.db_table)
    LOGGER.info("Dataset successfully imported")

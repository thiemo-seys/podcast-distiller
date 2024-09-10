import argparse

from src import db_utils


def create_db(fp: str):
    cursor = db_utils.open_connection(fp)
    db_utils.init_database(cursor)


def main():
    args = parser.parse_args()
    create_db(args.database)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-db",
        "--database",
        type=str,
        help="File path of the sqlite database",
        default="database/main.sqlite",
    )
    main()

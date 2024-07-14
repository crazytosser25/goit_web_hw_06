"""Module to generate database tables and fill them vith random data"""
import logging

from creatorium.structurum import create_structure
from creatorium.datum import generate_data


logging.basicConfig(
    level=logging.INFO,
    format='line_num: %(lineno)s > %(message)s'
)

def main():

    create_structure()
    logging.info('Structure created.')
    generate_data()
    logging.info('Data generated.')


if __name__ == "__main__":
    main()

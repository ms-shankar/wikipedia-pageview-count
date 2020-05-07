#!/usr/bin/python
"""This program is responsible for concurrently counting and aggregating the number of keyword occurrences
from all raw data files from the data lake
"""
import concurrent.futures
import logging
from app.utils.constants import DATALAKE_DIR
from app.helpers.aggregator_helper import get_stored_file_paths, process_file
import argparse

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

parser = argparse.ArgumentParser(description="Enter the configurable inputs")

parser.add_argument("-l",
                    action="store",
                    dest="language_code",
                    default="en",
                    help="Enter the language version of Wiki you want to process\n"
                         "Default: EN/en (English)")

parser.add_argument("-k",
                    action="store",
                    dest="keyword",
                    default="bitcoin",
                    help="Enter the keyword whose related page view you want to count\n"
                         "Default: bitcoin")

arguments = parser.parse_args()
language = arguments.language_code
keyword = arguments.keyword


def pageview_aggregator(datalake_dir):

    saved_paths = get_stored_file_paths(datalake_dir)

    # If files exist in the data storage directory
    if saved_paths:

        # Create concurrent processes and threads for processing files concurrently
        with concurrent.futures.ThreadPoolExecutor() as thread_ex:
            # ThreadPoolExecutor processes each file in a separate thread and aggregates the results.
            future_processed_files = [thread_ex.submit(process_file, language.lower(), keyword.lower(), path)
                                      for path in saved_paths]

            # File level aggregation completes and returns results
            aggregated_all = []
            for future in concurrent.futures.as_completed(future_processed_files):
                aggregated_all.append(future.result())

            logging.info(f"\tThe total wiki pageviews of sites pertaining to {keyword} in language {language} is: "
                         f"{sum(aggregated_all)}")

        logging.info('\tProcessing successfully completed')
        return sum(aggregated_all)

    # No files in the data directory
    else:
        logging.error(f"\tNo files found for processing in the data directory {DATALAKE_DIR}\n"
                      "Please run the ingestion job (ingest.py) and then run this aggregation")

        return -1


if __name__ == '__main__':
    pageview_aggregator(DATALAKE_DIR)

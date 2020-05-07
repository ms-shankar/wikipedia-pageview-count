#!/usr/bin/python
"""This program is responsible for concurrently gathering raw pageviews data from several urls
and storing the data into a local datalake for further processing.
"""
import concurrent.futures
import logging
from app.utils.constants import BASE_URL, DATALAKE_DIR
from app.helpers.ingestion_helper import get_download_paths, prepare_datalake, download_file

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def ingest_raw_wiki():
    # Get all downloadable links from the base url
    download_paths = get_download_paths(BASE_URL)

    # #TODO uncomment below for downloading minimal dataset
    # download_paths = [('https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/pagecounts-20160101-000000.gz',
    #                    'pagecounts-20160101-000000.gz'),
    #                   ('https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/pagecounts-20160101-010000.gz',
    #                    'pagecounts-20160101-010000.gz'),
    #                   ('https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/pagecounts-20160101-020000.gz',
    #                    'pagecounts-20160101-020000.gz')]

    # Prepare data storage directoy
    prepare_datalake()

    # Create concurrent processes and threads for downloading files concurrently
    with concurrent.futures.ThreadPoolExecutor() as thread_ex:
        # ThreadPoolExecutor downloads and saves each file in separate threads.
        future_download_files = [thread_ex.submit(download_file, path, DATALAKE_DIR) for path in download_paths]

    logging.info('\tIngestion successfully completed')


if __name__ == '__main__':
    ingest_raw_wiki()

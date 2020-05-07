import os

TEST_DIR = os.getcwd()

TEST_DATALAKE_DIR = os.path.join(TEST_DIR, "tests", "data", "datalake")
TEST_DATA_DIR = os.path.join(TEST_DIR, "tests", "data")

TEST_URL_1 = "https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/"
TEST_URL_2 = "https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-02/"
TEST_URL_3 = "https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-03/"

TEST_INPUT_1 = ('https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/pagecounts-20160101-000000.gz',
                'pagecounts-20160101-000000.gz')

TEST_INPUT_2 = ('https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/pagecounts-20160101-010000.gz',
                'pagecounts-20160101-010000.gz')

TEST_INPUT_3 = ('https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/pagecounts-20160101-020000.gz',
                'pagecounts-20160101-020000.gz')

TEST_OUT_1 = ['pagecounts-20160101-020000.gz', 'pagecounts-20160101-000000.gz', 'pagecounts-20160101-010000.gz']

TEST_FILE_PATH_1 = os.path.join(TEST_DATA_DIR, 'pagecounts-20160101-000000.gz')
TEST_FILE_PATH_2 = os.path.join(TEST_DATA_DIR, 'pagecounts-20160101-010000.gz')
TEST_FILE_PATH_3 = os.path.join(TEST_DATA_DIR, 'pagecounts-20160101-020000.gz')

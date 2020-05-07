import os

HOME_DIR = os.getcwd().split('/app/utils')[0]

BASE_URL = "https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/"

DATALAKE_DIR = os.path.join(HOME_DIR, "datalake")

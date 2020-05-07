from bs4 import BeautifulSoup
import requests
import os

from app.utils.constants import DATALAKE_DIR


def get_download_paths(url):
    """
    Fetches all raw data file links available in the base url
    :param url: A url containing links to raw data to be downloaded
    :return download_paths: A list containing paths to all downloadable raw data
    """
    download_paths = []
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, "html.parser")

    for link in soup.find_all('a'):
        filename = link.get('href')
        if ".gz" in filename:
            full_path = f"{url}{filename}"
            download_paths.append((full_path, filename))

    return download_paths


def prepare_datalake():
    """Create datalake directory if it does not exist already.
    """
    if not os.path.exists(DATALAKE_DIR):
        os.mkdir(DATALAKE_DIR)


def download_file(path, data_dir_path):
    """Downloads each raw data file using the resource path.
    :param path: A tuple containing download path and filename
    :param data_dir_path: Path to the data storage directory
    """
    download_path, filename = path

    save_path = os.path.join(data_dir_path, filename)

    if not os.path.exists(save_path):
        print(f'Downloading from filepath {download_path}')
        r = requests.get(download_path)
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print(f'Downloaded from filepath {download_path} successfully')
    else:
        print(f'File {save_path} already exists. No need to save again.')

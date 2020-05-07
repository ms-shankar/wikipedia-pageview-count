import os
import glob
import gzip


def get_stored_file_paths(data_dir):
    """
    Fetches file paths of all stored raw data files from the data storage dir
    :param data_dir: Local data storage directory path
    :return save: A list containing paths to all downloadable raw data
    """
    all_files = os.path.join(data_dir, f"*")
    file_paths_list = glob.glob(all_files)

    return file_paths_list


def process_file(language, keyword, path):
    """Processes each stored raw data file using the saved file path.
    :param language: Wiki language version for pageview count extraction
    :param keyword: Search term for pageview count extraction
    :param path: Saved file location
    :return file_count: A list of keyword occurrences in each file
    """

    search_string = f"{language} {keyword}"

    # Initialize counter list for each file
    count_in_file = []

    with gzip.open(path, 'rt') as f:
        for line in f:
            if line.startswith(search_string) or (line.startswith(language) and keyword in line):

                # Split lines into words
                words = line.split(' ')

                # Obtain pageviews in each line
                pageviews = words[-2]
                count_in_file.append(pageviews)

    # Convert string to int elements
    file_count = sum(int(i) for i in count_in_file)

    return file_count





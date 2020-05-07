from parameterized import parameterized
import unittest
from tests.utils.constants import TEST_DATALAKE_DIR, TEST_URL_1, TEST_URL_2, TEST_URL_3, TEST_INPUT_1, \
    TEST_INPUT_2, TEST_INPUT_3

import os
import os.path
import shutil

from app.helpers.ingestion_helper import get_download_paths, download_file


def get_download_paths_test_inputs():
    # parametrize input data and expected result as test case inputs
    return [
        (TEST_URL_1, 744),
        (TEST_URL_2, 696),
        (TEST_URL_3, 744)
    ]


def download_file_test_inputs():
    # parametrize input data as test case inputs
    return [
        (TEST_INPUT_1, 1),
        (TEST_INPUT_2, 2),
        (TEST_INPUT_3, 3)
    ]


class TestIngestionHelper(unittest.TestCase):

    # Ensure that the test data directory exists before running the tests
    def setUp(self):
        os.mkdir(TEST_DATALAKE_DIR)

    # Clean up test data directory to run the tests correctly next time
    def tearDown(self):
        shutil.rmtree(TEST_DATALAKE_DIR)

    @parameterized.expand(get_download_paths_test_inputs)
    def test_get_download_paths(self, input_url, expected_result):

        # Act
        result = get_download_paths(input_url)

        # Assert
        self.assertEqual(len(result), expected_result)

    @parameterized.expand(download_file_test_inputs)
    def test_download_file(self, test_input, test_run):
        # Arrange
        save_path = os.path.join(TEST_DATALAKE_DIR, test_input[1])

        # Act
        download_file(test_input, TEST_DATALAKE_DIR)

        # Assert
        self.assertTrue(os.path.exists(save_path))


if __name__ == '__main__':
    unittest.main()

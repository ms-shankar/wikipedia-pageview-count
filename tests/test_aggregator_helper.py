from parameterized import parameterized
import unittest
from tests.utils.constants import TEST_DATA_DIR, TEST_OUT_1, TEST_FILE_PATH_1, TEST_FILE_PATH_2, TEST_FILE_PATH_3

from app.helpers.aggregator_helper import get_stored_file_paths, process_file


def process_file_test_inputs():
    # parametrize input data and expected result as test case inputs
    return [
        ('en', 'bitcoin', TEST_FILE_PATH_1, 156),
        ('en', 'bitcoin', TEST_FILE_PATH_2, 19),
        ('en', 'bitcoin', TEST_FILE_PATH_3, 154),
        ('en', 'java', TEST_FILE_PATH_1, 8),
        ('en', 'java', TEST_FILE_PATH_2, 8),
        ('de', 'java', TEST_FILE_PATH_1, 10),
    ]


class TestAggregatorHelper(unittest.TestCase):

    def test_get_stored_file_paths(self):

        # Act
        full_path_list = get_stored_file_paths(TEST_DATA_DIR)
        stripped_path_list = []
        for path in full_path_list:
            stripped_path = path.split('/tests/data/')[1]
            stripped_path_list.append(stripped_path)

        # Assert
        self.assertEqual(stripped_path_list, TEST_OUT_1)

    @parameterized.expand(process_file_test_inputs)
    def test_process_file(self, language, keyword, file_path, expected_result):

        # Act
        result = process_file(language, keyword, file_path)

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

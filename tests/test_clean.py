import unittest
import pandas as pd

from task1.clean import filter_data


class TestCleanData(unittest.TestCase):
    """
    A class for unit-testing all functions in the clean.py file

    Args:
    -----
    unittest.TestCase this allows the new class to inherit
    from the unittest module
    """

    def setUp(self) -> pd.DataFrame:
        self.df = pd.read_csv("../data/sample_test_data.csv")

    def test_filter_data(self):
        column_name = "SiteID"
        df = filter_data(self.df)
        missing_count = df[column_name].isna().sum()
        self.assertEqual(missing_count, 0, "Value should be zero")


if __name__ == "__main__":
    unittest.main()

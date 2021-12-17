import sys
import os
import unittest
import pandas as pd

sys.path.append(os.path.abspath(os.path.join("../")))

from task1.crop import crop_data


class TestCropData(unittest.TestCase):
    """
    A class for unit-testing function in the fix_clean_tweets_dataframe.py file

    Args:
    -----
    unittest.TestCase this allows the new class to inherit
    from the unittest module
    """

    def setUp(self) -> pd.DataFrame:
        self.df = pd.read_csv("../data/sample_test_data.csv")

    def test_crop_data(self):
        date_value = "2010-01-01T00:00:00+00:00"
        new_df = crop_data(self.df)
        new_df.reset_index(drop=True)
        self.assertGreaterEqual(
            new_df["Date Time"][0],
            date_value,
            f"It needs to be greater than or Equal to {date_value}",
        )


if __name__ == "__main__":
    unittest.main()

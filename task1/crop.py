# Crop the file to delete  any records before 00:00 1 jan 2010 (1262304000).
import pandas as pd
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s - Crop data - %(message)s", level=logging.INFO
)
logging.getLogger().setLevel(logging.INFO)


def crop_data(df: pd.DataFrame, date_value: str = "2010-01-01T00:00:00+00:00"):
    logging.info(f"Total record Before cropping is: {df.shape}")
    new_df = df[df["Date Time"] >= date_value]
    logging.info(f"Total record After cropping is: {new_df.shape}")
    return new_df


if __name__ == "__main__":
    df = pd.read_csv("../data/bristol-air-quality-data.csv", sep=";")
    new_df = crop_data(df)

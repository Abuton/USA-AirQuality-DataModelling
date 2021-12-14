"""
Filter for and remove any dud records where there is no value for SiteID
or there is a mismatch between SiteID and Location.
(This script should print the lines number and
mismatch field values for each dud record.)
"""
import pandas as pd
import warnings
from crop import crop_data

warnings.filterwarnings("ignore")

mappings = {
    188: "AURN Bristol Centre",
    203: "Brislington Depot",
    206: "Rupert Street",
    209: "IKEA M32",
    213: "Old Market",
    215: "Parson Street School",
    228: "Temple Meads Station",
    270: "Wells Road",
    271: "Trailer Portway P&R",
    375: "Newfoundland Road Police Station",
    395: "Shiner's Garage",
    452: "AURN St Pauls",
    447: "Bath Road",
    459: "Cheltenham Road \ Station Road",
    463: "Fishponds Road",
    481: "CREATE Centre Roof",
    500: "Temple Way",
    501: "Colston Avenue",
}


def filter_data(df):
    # filter out missing site ID
    missing_site_id = df[pd.isnull(df["SiteID"])]
    df = df.dropna(subset=["SiteID"])
    print("missing SiteID row numbers are", missing_site_id.index.values)
    return df


# mismatch
def remove_mismatch(df):
    df.reset_index(drop=True, inplace=True)
    mismatch = []
    for i, val in enumerate(df["SiteID"].astype(int)):
        if val in mappings.keys():
            if df["Location"][i] != mappings[val]:
                mismatch.append(1)
                print(
                    f"line number mismatch is {i}, mismatch SiteID = {df['SiteID'][i]}, Mistmatch Location = {df['Location'][i]}"
                )
            else:
                mismatch.append(0)
        else:
            print(
                    f"line number mismatch is {i}, mismatch SiteID = {df['SiteID'][i]}, Mistmatch Location = {df['Location'][i]}"
                )
            mismatch.append(1)

    # drop mismatch rows
    df["mismatch"] = mismatch
    print("Total Rows Before Dropping mismatch:", df.shape[0])
    df = df[df["mismatch"] == 0]
    df.drop(columns=["mismatch"], axis=1, inplace=True)
    print("Total Rows After Dropping mismatch:", df.shape[0])
    df.to_csv('cleaned_bristol-air-quality-data.csv', index=False)
    return df


if __name__ == "__main__":
    df = pd.read_csv("../bristol-air-quality-data.csv", sep=";")
    cropped_df = crop_data(df)
    filtered_df = filter_data(cropped_df)
    remove_mismatch_df = remove_mismatch(filtered_df)
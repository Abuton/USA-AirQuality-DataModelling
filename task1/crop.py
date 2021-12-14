# Crop the file to delete  any records before 00:00 1 jan 2010 (1262304000).

def crop_data(df):
    print("Total record Before cropping is: ", df.shape)
    new_df = df[df['Date Time'] >= '2010-01-01T00:00:00+00:00']
    print("Total record After cropping is: ", new_df.shape)
    return new_df


if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("../bristol-air-quality-data.csv", sep=';')
    new_df = crop_data(df)

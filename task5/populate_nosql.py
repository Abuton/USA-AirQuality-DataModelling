from pymongo import MongoClient
import pandas as pd
import logging
import json

logging.basicConfig(
    format="%(asctime)s %(levelname)s - NoSQL PopulateDB - %(message)s",
    level=logging.INFO,
)
logging.getLogger().setLevel(logging.INFO)


def connectMongo():
    try:
        conn = MongoClient()
        logging.info("Connected Succesfully!")
        return conn
    except Exception as e:
        logging.error(f"An Error Occured {e}")


def csv_to_json(filename, header=None):
    data = pd.read_csv(filename, header=header, low_memory=False)
    data.fillna(0, inplace=True)
    return json.loads(data.to_json(orient="records"))


if __name__ == "__main__":
    database_name = "pollution_nosql"
    table_name = "BrislingtonDepot"
    conn = connectMongo()
    # connect to the database
    db = conn[database_name]
    # create a new table
    collection = db[table_name]

    records = csv_to_json("../data/Brislington_Depot.csv")
    # recs = records[:10]
    if collection.count_documents({}) > 0:
        logging.info("Removing documents from db")
    else:
        try:
            # inserting the data in the database
            collection.insert_many(records)
            print("Records inserted")
        except Exception as e:
            print("Error Occured", e)

# for i in collection.find({'title': 'MongoDB and Python'}):
#     print(i)

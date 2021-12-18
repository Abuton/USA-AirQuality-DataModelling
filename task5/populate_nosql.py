from pymongo import MongoClient
import pandas as pd
import logging

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


def csv_to_json(filename: str):
    data = pd.read_csv(filename, low_memory=False)
    # data.fillna(0, inplace=True)
    return data.to_dict(orient="records")


def insert_into_mongodb(filename: str = "../data/clean_Brislington_Depot.csv"):
    records = csv_to_json(filename)
    collection.insert_many(records)
    logging.info("Records inserted Successfully:")


if __name__ == "__main__":
    database_name = "pollution_nosql"
    table_name = "BrislingtonDepot"

    conn = connectMongo()
    # connect to the database
    db = conn[database_name]
    # create a new table
    collection = db[table_name]

    if collection.count_documents({}) > 0:
        count = collection.delete_many({})
        logging.info(f"{count} documents deleted.")
        insert_into_mongodb()
    else:
        try:
            insert_into_mongodb()
        except Exception as e:
            logging.error(f"Error Occured {e}")

    logging.info(f"Total Documents = {collection.count_documents({})}")

# db.BrislingtonDepot.find( {NOx: {$gt: 30 } } )

# for i in collection.find({'title': 'MongoDB and Python'}):
#     print(i)

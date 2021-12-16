from pymongo import MongoClient
import pandas as pd


def connectMongo():
    try:
        conn = MongoClient()
        print("Connected Succesfully!")
        return conn
    except Exception as e:
        print("An Error Occured", e)


def csv_to_json(filename, header=None):
    data = pd.read_csv(filename, header=header)
    return data.to_dict('records')


if __name__ == "__main__":
    database_name = "pollution_nosql"
    table_name = "BrislingtonDepot"
    conn = connectMongo()
    # connect to the database
    db = conn[database_name]

    # create a new table
    collection = db[table_name]

    records = csv_to_json("../data/Brislington_Depot.csv")
    recs = records[:10]
    try:
        # inserting the data in the database
        collection.insert_many(recs)
        print("Records inserted")
    except Exception as e:
        print("Error Occured", e)

# for i in collection.find({'title': 'MongoDB and Python'}):
#     print(i)

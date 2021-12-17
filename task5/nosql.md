# NoSQL Data Model

A NoSQL database provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases. Such databases like mysql have existed since the late 1960s, but the name "NoSQL" was only coined in the early 21st century, triggered by the needs of Web 2.0 companies. NoSQL is an acronym which means **Not only SQL**. It is an approach to database management that can accommodate a wide variety of data models, including key-value, document, columnar and graph formats. A NoSQL database generally means that it is non-relational, distributed, flexible and scalable. Additional common NoSQL database features include the lack of a database schema, data clustering, replication support and eventual consistency, as opposed to the typical ACID (atomicity, consistency, isolation and durability) transaction consistency of relational and SQL databases.

There are many NoSQL database implementation and I have selected the MongoDB NoSQL to model the Air Quality Data.

**MongoDB**, the most popular NoSQL database, is an open-source document-oriented database. MongoDB is not based on the table-like relational database structure but provides an altogether different mechanism for storage and retrieval of data. This format of storage is called BSON ( similar to JSON format).

A Simple Example would look like this

```
{
    "Date Time": 2020/09/21 08:00:00,
    "NOx": 54.3,
    "PM2.5": 0.4,
    "PM10": 12
}
```
For this task, I will be creating a MongoDB Database instance and will create a table known as collection. I will be using the `pymongo` python library to interact with MongoDB API and load data into the database as well as query it.

I have choosen MongoDB because of it popularity, ease of Use and setup. Plus it also free.

The task requires loading all rows for a specific Site in my case, I will be extracting the datapoints recorded from the **Brislington Depot** Station. I like the name that's why.

After Extraction which will be achieved by a query that looks like this in sql
    `SELECT * FROM 'pollution-db' WHERE Location = 'Brislington Depot'`

The same result can be achieved using the pandas library as shown below:
    `bris_station_df = df[df['Location'] == 'Brislington Depot']`

On successful extraction, I will create a connection to my MongoDB instance using pymongo as follows:
    ```
        from pymongo import MongoClient
        def connectMongo():
            try:
                conn = MongoClient()
                print("Connected Succesfully!")
                return conn
            except Exception as e:
                print(f"An Error Occured {e}")

    ```
Then I will create a database and a collection to store the station data. Since MongoDB is a Document/ Key-Value pair kind of database, the relational table-like format won't work. Hence, I need to convert the csv station data into a json format. Below is the code to do just that;
    ```
        def csv_to_json(filename, header=None):
            data = pd.read_csv(filename, header=header, low_memory=False)
            return data.to_dict('records')
    ```



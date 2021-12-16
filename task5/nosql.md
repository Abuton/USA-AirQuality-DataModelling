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



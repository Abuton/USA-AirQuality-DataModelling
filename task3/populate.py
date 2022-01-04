import pandas as pd
import mysql.connector as mysql
import sys


def DBConnect(dbName=None):
    """

    Parameters
    ----------
    dbName :
        Default value = None)

    Returns
    -------

    """
    conn = mysql.connect(host="localhost", user="root",
                         database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur


def createDB(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:

    Returns
    -------

    """
    try:
        conn, cur = DBConnect(dbName)
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
        conn.commit()
        print(f"{dbName} DataBases Successfully created")
        cur.close()
    except Exception as e:
        print("Error:", e)


def createTables(dbName: str) -> None:
    """
    Parameters
    ----------
    dbName :
        str:

    Returns
    -------
    """
    conn, cur = DBConnect(dbName)
    sqlFile = "air_pollution_schema.sql"
    fd = open(sqlFile, "r")
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(";")

    for command in sqlCommands:
        try:
            _ = cur.execute(command)
            print(f"Tables Successfully created in {dbName}")
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return None


def insert_to_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str: the table name

    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (DateRecorded, SiteID, Location,
                     NO2, NOX, NO, PM10, PM2.5, NVPM10, NVPM2.5,
                     VPM10, VPM2.5, CO, O3, Temperature,
                     ReletiveHumidity, AirPressure, GeoPoint2d,
                     CurrentStatus, InstrumentType, StartDateTime, EndDateTime)
                     VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                     %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        data = (
            row[0],
            row[4],
            row[17],
            row[2],
            row[1],
            row[3],
            row[5],
            row[9],
            row[6],
            row[8],
            row[7],
            row[10],
            row[11],
            row[12],
            row[14],
            row[15],
            row[16],
            row[18],
            row[21],
            row[22],
            row[19],
            row[20],
        )

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
            sys.exit()
    return None


if __name__ == "__main__":
    dbName = "pollution-db2"
    table_name = "AirQualityMeasures"
    df = pd.read_csv("../data/cleaned_bristol-air-quality-data.csv",
                     low_memory=False)

    # create db
    createDB(dbName)
    # create table
    createTables(dbName)
    # insert into tables
    insert_to_table(dbName, df, table_name)

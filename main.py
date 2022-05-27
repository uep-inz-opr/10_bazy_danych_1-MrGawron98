import sqlite3
import csv

def main():
    connection = sqlite3.connect("mydatabase.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = connection.cursor()
    cursor.execute("SELECT sum(duration) FROM polaczenia")
    print(cursor.fetchone()[0])
    # cursor.execute(
    #     "CREATE TABLE polaczenia (from_subscriber data_type INTEGER, to_subscriber data_type INTEGER, datetime data_type timestamp, duration data_type INTEGER, celltower data_type INTEGER);")
    # connection.commit()

    # with open("polaczenia_duze.csv", 'r') as file:
    #     reader = csv.reader(file, delimiter = ";")
    #     headers = next(reader)
    #     rows = [x for x in reader]
    #     cursor.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration, celltower) VALUES (?,?,?,?,?);", rows)
    #     connection.commit()
    #
    # print("success")


if __name__ == "__main__":
    main()

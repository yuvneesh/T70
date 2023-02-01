import sqlite3


def add_sample(database: str, sample: dict):
    """ Function to initialize the database and add sample data 
    ---------------------------------------
    Parameters

    database: Path/name of database file
    sample: A dictionary object of sample_type 
    """
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS samples (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sample_id TEXT,
                size TEXT,
                result TEXT,
                start_time TEXT
                )""")
    conn.commit()

    c.execute("""INSERT INTO samples (sample_id, size, result, start_time)
                VALUES (?,?,?,?)""", 
                (sample['id'], 
                 sample['size'],
                 sample['result'],
                 sample['start_time']))
    conn.commit()

    conn.close()



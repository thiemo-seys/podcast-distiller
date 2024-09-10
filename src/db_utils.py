import hashlib
import sqlite3

KILOBIT_SIZE = 1024


def open_connection(file: str):
    return sqlite3.connect(file)


def calculate_blake2(file_path: str, chunk_size=128 * KILOBIT_SIZE):
    hash = hashlib.blake2b()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash.update(chunk)

    return hash.hexdigest()


def init_database(cursor):
    query = """
    CREATE TABLE IF NOT EXISTS transcriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        file_hash TEXT
        transcription_model TEXT
        text TEXT
        created_at TEXT
        updated_at TEXT
    )
    """
    return cursor.execute(query)

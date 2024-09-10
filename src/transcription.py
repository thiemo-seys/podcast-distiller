from dataclasses import dataclass
from datetime import datetime


def result_to_model(result):
    return Transcription(
        text=result["text"],
        transcription_model=result["transcription_model"],
        input_file=result["input_file"],
    )


@dataclass
class Transcription:
    id: str
    text: str
    transcription_model: str
    input_file: str
    file_hash: str
    created_at: datetime
    updated_at: datetime


class TranscriptionRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self._table_name = "transcriptions"

    def create_transcription(self, transcription: Transcription):
        """
        Saves a transcription to the database.
        """
        current_time = datetime.now()
        transcription.created_at = current_time
        transcription.updated_at = current_time

        query = "INSERT INTO transcriptions (text, transcription_model, input_file, file_hash) VALUES (?, ?, ?)"
        return self.db_connection.execute(
            query,
            (
                transcription.text,
                transcription.transcription_model,
                transcription.input_file,
                transcription.file_hash,
                transcription.created_at,
                transcription.updated_at,
            ),
        )

    def update_transcription(self, transcription: Transcription, strict=True, **params):
        if strict and transcription.id is None:
            raise ValueError(
                "Can't update a transcription that has not been stored in the database already"
            )

        query = self._base_update_clause()
        query += "".join(f"{column} = ?" for column in params.keys())
        query += " WHERE id = ?"
        return self.db_connection.execute(query, (*params.values(), transcription.id))

    def find_by_id(self, transcription_id: int) -> tuple:
        """
        Retrieves a transcription from the database by its ID.
        """
        query = f"{self._base_select_clause()} WHERE id = ? LIMIT 1"
        result = self.db_connection.execute(query, (transcription_id,)).fetchone
        return result

    def find_by(self, strict=True, **params) -> tuple:
        """
        Retrieves a transcription from the database by the given params
        """
        if not params:
            raise ValueError("Please provide params when using find_by")

        query = f"{self._base_select_clause()}  WHERE "
        query += " AND ".join([f"{column} = ?" for column, value in params.items()])
        query += " LIMIT 1"
        print(f"{query=}")

        result = self.db_connection.execute(query, (params.values())).fetchone
        if strict and result is None:
            raise ValueError("No transcription found with given params")

        return result

    def _base_select_clause(self):
        return f"SELECT * FROM {self._table_name}"

    def _base_update_clause(self):
        return f"UPDATE {self._table_name} SET"

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")

    @staticmethod
    def validate():
        history_file = os.getenv("HISTORY_FILE")

        if history_file is not None and not history_file.strip():
            raise ValueError("HISTORY_FILE cannot be empty")
import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Config:
    @classmethod
    def get_database_url(cls) -> str:
        return os.getenv(
            "DATABASE_URL", "postgresql://user:password@localhost:5432/lib_db"
        )

    @classmethod
    def get_storage_type(cls) -> str:
        return os.getenv("STORAGE_TYPE", "memory")

    @classmethod
    def get_json_dir(cls) -> str:
        return os.getenv("JSON_DATA_DIR", "/tmp/lib_data")

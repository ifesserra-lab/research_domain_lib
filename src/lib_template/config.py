import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/lib_db")
    STORAGE_TYPE = os.getenv("STORAGE_TYPE", "memory")
    JSON_DATA_DIR = os.getenv("JSON_DATA_DIR", "/tmp/lib_data")

    @classmethod
    def get_database_url(cls) -> str:
        return cls.DATABASE_URL

    @classmethod
    def get_storage_type(cls) -> str:
        return cls.STORAGE_TYPE

    @classmethod
    def get_json_dir(cls) -> str:
        return cls.JSON_DATA_DIR

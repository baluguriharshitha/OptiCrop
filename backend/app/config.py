from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/opticrop"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "opticrop-secret-key-change-me"
    )

    ALGORITHM = os.getenv(
        "ALGORITHM",
        "HS256"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES",
            60
        )
    )


settings = Settings()

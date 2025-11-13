import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
        JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-dev-secret")
            JWT_ACCESS_TOKEN_EXPIRES = 3600  # segundos (1h)
                DATABASE = os.environ.get("DATABASE_URL", "db.sqlite3")
                
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import BaseConfig

SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI


def create_connection():
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        return engine

    except Exception as e:
        print(e)


create_eng = create_connection()
SessionLocal = sessionmaker(
    bind=create_eng,
    autocommit=False,
    autoflush=True,
    expire_on_commit=False
)


class SqlContext(object):
    def __init__(self):
        self.session = SessionLocal()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.session:
            try:
                self.session.commit()
            except Exception as ex:
                self.session.rollback()
                raise ex

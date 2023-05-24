from sqlalchemy.orm import Session


class Repository:
    def __init__(self, engine):
        self.engine = engine

    def insert_objects(self, batch):
        with Session(self.engine) as session:
            session.add_all(batch)
            session.commit()

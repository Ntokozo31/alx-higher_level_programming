#!/usr/bin/python3
"""
This script lists all City objects from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accesses the database and retrieves the city data.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    )
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

#!/usr/bin/python3
"""
Fetches all City objects from the database hbtn_0e_14_usa
and prints them with their state name.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

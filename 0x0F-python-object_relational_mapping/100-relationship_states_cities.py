#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]
    )
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()

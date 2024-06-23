#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the database connection string
    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    db_url = f"mysql+mysqldb://{db_user}:{db_pass}@localhost/{db_name}"
    # Create the engine
    engine = create_engine(db_url)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()
    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
    # Close the session
    session.close()

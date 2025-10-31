#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
as <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Join State and City tables and order by city ID
    results = (
        session.query(State, City)
        .join(City)
        .order_by(City.id)
        .all()
    )

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

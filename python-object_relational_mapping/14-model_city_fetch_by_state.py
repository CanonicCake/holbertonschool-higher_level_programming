#!/usr/bin/python3
"""List all State and city objects from hbtn_0e_6_usa"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State).all()
    for city, state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.commit()

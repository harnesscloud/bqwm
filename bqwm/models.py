from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class JobConfiguration(Base):
    __tablename__ = 'job_configurations'

    id = Column(Integer, primary_key=True)
    utility_function = Column(String(64))
    estimated_time = Column(Integer)
    price = Column(Integer)

    def __init__(self, utility_function, estimated_time, price):
        self.utility_function = utility_function
        self.estimated_time = estimated_time
        self.price = price

    def __repr__(self):
        return 'JobConfiguration: {} {} {}'.format(
            self.utility_function, self.estimated_time, self.price)

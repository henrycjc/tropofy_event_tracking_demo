"""
This is a demo app not intended for use in production. 

Author  : Henry Chladil <henry.ponco@gmail.com>
Created : 2017-JUL-9
Modified: 2017-JUL-9
"""
from sqlalchemy.types import Text, Float, Integer, DateTime
from sqlalchemy.schema import Column, ForeignKey
from tropofy.database.tropofy_orm import DataSetMixin
from tropofy.app import AppWithDataSets, Step, StepGroup
from tropofy.widgets import SimpleGrid
from collections import OrderedDict


class Station(DataSetMixin):
    """
    Represents a ride/attraction at an event. Lat/long there to make heatmapping possible.

    """
    __tablename__ = "station"

    station_name = Column(Text, unique=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    price = Column(Integer, nullable=True)


class Entry(DataSetMixin):

    __tablename__ = "entry"
    
    station = Column(Text, ForeignKey('station.station_name'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    

class EventTrackingDemoApp(AppWithDataSets):

    def get_name(self):
        return "Event Tracking Demo"

    def get_gui(self):
        return OrderedDict([
            ('stores', StepGroup(
                name='Stores',
                steps=OrderedDict([
                    ('stores', Step(
                        name='Stores',
                        widgets=[SimpleGrid(Station)]
                    ))
                ]),
            )),
        ])

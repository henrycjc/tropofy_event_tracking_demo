"""
This is a demo app not intended for use in production.

Author  : Henry Chladil <henry.ponco@gmail.com>
Created : 2017-JUL-9
Modified: 2017-JUL-9
"""
import datetime
from sqlalchemy.types import Text, Float, Integer, DateTime
from sqlalchemy.schema import Column, ForeignKey
from tropofy.database.tropofy_orm import DataSetMixin
from tropofy.app import AppWithDataSets, Step, StepGroup
from tropofy.widgets import SimpleGrid, TimelineWidget


class Station(DataSetMixin):
    """
    Represents a ride/attraction/stall at an event. Lat/long there to make heatmapping possible.

    """
    station_name = Column(Text, unique=True)
    station_type = Column(Text, nullable=False)  # e.g. food, ride, entertainment
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    price = Column(Integer, nullable=True)


class Food(DataSetMixin):
    station = Column(Text, ForeignKey('station.station_name'), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Text, nullable=False)  # Can't use float because reasons


class Entry(DataSetMixin):
    station = Column(Text, ForeignKey('station.station_name'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    age = Column(Integer, nullable=True)
    postcode = Column(Integer, nullable=True)

    @property
    def serialise(self):
        """
        Get a dict representation of a record. Could be a classmethod.
        :return: dict representation of current state of the sql record
        """
        return {
            "station": self.station,
            "timestamp": self.timestamp,
            "age": self.age,
            "postcode": self.postcode
        }


class EventTrackingDemoApp(AppWithDataSets):
    def get_name(self):
        return "Event Tracking Demo"

    def get_gui(self):
        return [
            StepGroup(
                name='Stations',
                steps=[
                    Step(
                        name='Overview',
                        widgets=[SimpleGrid(Station)]
                    ),
                    Step(
                        name='Foods',
                        widgets=[SimpleGrid(Food)]
                    ),
                ]
            ),
            StepGroup(
                name='Usage',
                steps=[
                    Step(
                        name='Overview',
                        widgets=[SimpleGrid(Entry),
                                 ExampleTimelineWidget()]
                    )
                ]
            )
        ]

class ExampleTimelineWidget(TimelineWidget):
    def get_title(self, app_session):
        return 'Work shifts'

    def get_options(self, app_session):
        return {
            'hiddenDates': [
                {
                    'start': datetime.datetime(2017, 1, 2, 18),
                    'end': datetime.datetime(2017, 1, 3, 6)
                }
            ]
        }

    def get_data(self, app_session):
        return [
            {'id': 1, 'group': 'John', 'content': 'Monday Shift 1', 'start': datetime.datetime(2017, 1, 2, 7),
             'end': datetime.datetime(2017, 1, 2, 12)},
            {'id': 2, 'group': 'John', 'content': 'Tuesday Shift 2', 'start': datetime.datetime(2017, 1, 3, 12),
             'end': datetime.datetime(2017, 1, 3, 17)},
            {'id': 3, 'group': 'Sarah', 'content': 'Monday Shift 2', 'start': datetime.datetime(2017, 1, 2, 11),
             'end': datetime.datetime(2017, 1, 2, 17)},
            {'id': 4, 'group': 'Sarah', 'content': 'Tuesday Shift 1', 'start': datetime.datetime(2017, 1, 3, 7),
             'end': datetime.datetime(2017, 1, 3, 12)},
        ]

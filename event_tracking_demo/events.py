"""
This is a demo app not intended for use in production. 

Author  : Henry Chladil <henry.ponco@gmail.com>
Created : 2017-JUL-9
Modified: 2017-JUL-9
"""
from sqlalchemy.types import Text, Float
from sqlalchemy.schema import Column
from tropofy.database.tropofy_orm import DataSetMixin
from tropofy.app import AppWithDataSets, Step, StepGroup
from tropofy.widgets import SimpleGrid
from collections import OrderedDict

class Store(DataSetMixin):
    name = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)


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
                        widgets=[SimpleGrid(Store)]
                    ))
                ]),
            )),
        ])

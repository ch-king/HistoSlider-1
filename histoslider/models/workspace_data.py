import jsonpickle

from histoslider.models.base_data import BaseData
from histoslider.models.slide_data import SlideData


class WorkspaceData(BaseData):
    def __init__(self, name: str):
        super().__init__(name)

    def add_slide(self, slide: SlideData):
        self.addChild(slide)

    def to_json(self):
        return jsonpickle.encode(self)

    @classmethod
    def from_json(cls, json):
        return jsonpickle.decode(json)
from __future__ import annotations

from typing import List

from PyQt5.QtGui import QIcon

from histoslider.models.acquisition_channel import AcquisitionChannel
from histoslider.models.acquisition_meta import AcquisitionMeta
from histoslider.models.base_data import BaseData


class Acquisition(BaseData):
    def __init__(self, meta: AcquisitionMeta):
        super().__init__(meta.description)
        self.meta = meta

    def add_channel(self, channel: AcquisitionChannel):
        self.addChild(channel)

    @property
    def acquisition_roi(self) -> "AcquisitionROI":
        return self.parent()

    @property
    def icon(self):
        return QIcon(":/icons/icons8-film-roll-16.png")

    @property
    def tooltip(self):
        return "Acquisition"

    @property
    def channels(self) -> List[AcquisitionChannel]:
        return self._children

from pyqtgraph import GraphicsView, GraphicsLayout

from histoslider.core.hub_listener import HubListener
from histoslider.core.manager import Manager
from histoslider.core.message import ChannelImagesChangedMessage
from histoslider.ui.histogram_view import HistogramView


class HistogramsView(GraphicsView, HubListener):
    def __init__(self, parent=None, blend_view=None):
        GraphicsView.__init__(self, parent)
        HubListener.__init__(self)
        self.register_to_hub(Manager.hub)
        self.blend_view = blend_view

        self.layout = GraphicsLayout()
        self.setCentralItem(self.layout)

    def register_to_hub(self, hub):
        hub.subscribe(self, ChannelImagesChangedMessage, self._on_channel_images_changed)

    def _on_channel_images_changed(self, message: ChannelImagesChangedMessage):
        self.layout.clear()
        for item in message.images:
            histogram_view = HistogramView(item, self.blend_view)
            self.layout.addItem(histogram_view)

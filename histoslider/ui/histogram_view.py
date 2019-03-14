from pyqtgraph import HistogramLUTItem

from histoslider.image.channel_image_item import ChannelImageItem


class HistogramView(HistogramLUTItem):
    def __init__(self, image_item: ChannelImageItem, blend_view=None):
        HistogramLUTItem.__init__(self)
        self.gradient.hide()
        self.setImageItem(image_item)
        self.blend_view = blend_view
        self.channel = image_item.channel
        self.setLevels(*self.channel.settings.levels)
        self.sigLevelChangeFinished.connect(self._on_level_change_finished)
        self.sigLookupTableChanged.connect(self._on_lookup_table_changed)

    def _on_level_change_finished(self):
        if self.channel is None:
            return
        self.channel.settings.levels = self.getLevels()
        if self.blend_view is not None:
            self.blend_view.refresh_images()

    def _on_lookup_table_changed(self):
        if self.channel is None:
            return
        lut = self.getLookupTable(n=int(self.channel.settings.levels[1]), alpha=0.5)
        self.channel.settings.lut = lut
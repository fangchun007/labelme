# -*- encoding: utf-8 -*-

from qtpy.QtCore import Qt
from qtpy import QtWidgets

from .escapable_qlist_widget import EscapableQListWidget


class UniqueLineWidthQListWidget(EscapableQListWidget):
    def mousePressEvent(self, event):
        super(UniqueLineWidthQListWidget, self).mousePressEvent(event)
        if not self.indexAt(event.pos()).isValid():
            self.clearSelection()

    def findItemsByLineWidth(self, line_width):
        items = []
        for row in range(self.count()):
            item = self.item(row)
            if item.data(Qt.UserRole) == line_width:
                items.append(item)
        return items

    def createItemFromLineWidth(self, line_width):
        item = QtWidgets.QListWidgetItem()
        item.setData(Qt.UserRole, line_width)
        return item

    def setItemLineWidth(self, item, line_width, color=None):
        qlinewidth = QtWidgets.QLabel()
        if color is None:
            qlinewidth.setText("{}".format(line_width))
        else:
            qlinewidth.setText(
                '{} <font color="#{:02x}{:02x}{:02x}">●</font>'.format(
                    line_width, *color
                )
            )
        qlinewidth.setAlignment(Qt.AlignBottom)

        item.setSizeHint(qlinewidth.sizeHint())

        self.setItemWidget(item, qlinewidth)

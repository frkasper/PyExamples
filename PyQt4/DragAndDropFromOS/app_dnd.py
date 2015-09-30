import sys
from PyQt4 import QtCore, QtGui, uic


_sig_clk = QtCore.SIGNAL('clicked()')


class MyApp(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.__init_form()

    def __init_form(self):
        uic.loadUi('formUI.ui', self)
        self.__init_items()
        self.__init_lv1()

    def __init_items(self):
        self.connect(self.pb1, _sig_clk, sys.exit)

    def __init_lv1(self):
        self.qm1 = QtGui.QStandardItemModel(self.lv1)
        self.lv1.setModel(self.qm1)

    def add_item(self, item):
        qitem = QtGui.QStandardItem(item)
        self.qm1.appendRow(qitem)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = MyApp()
    form.add_item('An example item.')
    form.add_item('Another example item.')
    form.show()
    app.exec_()

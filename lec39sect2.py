import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import PlotWidget
import numpy as np

x = np.array([1,2,3])
y = np.array([1,2,3])
pg.setConfigOption('background', 'w')
penn = pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine)
p1 = pg.plot(x, y, pen = penn, title='The first pyqtgraph plot', symbol='t', symbolSize=20)
p1.setXRange(0,4)
p1.setYRange(0,4)
p1.setLabel('left', 'Voltage', 'V')
p1.setLabel('bottom', 'Time', 's')

QtGui.QApplication.exec_()


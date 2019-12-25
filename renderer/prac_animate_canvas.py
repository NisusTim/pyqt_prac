import matplotlib
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg \
  as FigureCanvas
from PyQt5 import QtWidgets
import numpy as np

# Ensure using PyQt5 backend.
matplotlib.use('QT5Agg')
# Display negative sign normally.
matplotlib.rcParams["axes.unicode_minus"] = False

# Matplolib canvas class to create figure
class CanvasRenderer(FigureCanvas):
  zh_font = matplotlib.font_manager.FontProperties(
    fname=r"/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
    # fname=r"/usr/share/fonts-droid-fallback/truetype/DroidSansFallback.ttf")

  def __init__(self, width=5, height=4, dpi=100, layout_int=111):
    self.fig = Figure(figsize=(width, height), dpi=dpi)
    self.fig.suptitle("正弦波 sin wave", fontproperties=self.zh_font)

    self.axes = self.fig.add_subplot(layout_int)
    self.axes.clear()
    self.axes.grid(True)

    # super() = FigureCanvas, which the parent class is
    # FigureCanvas.__init__(self, self.fig)
    # FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding,
    #                            QtWidgets.QSizePolicy.Expanding)
    # FigureCanvas.updateGeometry(self)
    super().__init__(self.fig)
    super().setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                          QtWidgets.QSizePolicy.Expanding)
    super().updateGeometry()

    self.DrawStaticImage()

  def DrawStaticImage(self):
    # Generate data
    self.x = np.linspace(0, 20, 100)
    self.y = np.sin(self.x)

    # Plot
    self.axes.set_xlim(0, 20)
    self.axes.plot(self.x, self.y, "c")

    self.axes.set_xlabel("時間 time", fontproperties=self.zh_font)
    self.axes.set_ylabel("振幅 amplitude", fontproperties=self.zh_font)
    self.axes.grid(True)
    self.draw()

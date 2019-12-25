import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from view.prac_animate_ui import UiMainWindow
from renderer.prac_animate_canvas import CanvasRenderer

class MainWindow(QMainWindow):

  def __init__(self, parent=None):
    super().__init__(parent=parent)
    self.Ui = UiMainWindow()
    self.Ui.SetupUi(self)
    self.ConnectSlot()
    self.AddCanvasToWidget(self.Ui.plot_widget)

  def ConnectSlot(self):
    self.Ui.button.clicked.connect(self.BtnOnClicked)

  def BtnOnClicked(self):
    print("Button pressed.")

  def AddCanvasToWidget(self, parent=None):
    self.canvas_renderer = CanvasRenderer()
    parent.addWidget(self.canvas_renderer)

app = None
window = None

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

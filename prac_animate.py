import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

class MainWindow(QMainWindow):

  def __init__(self, parent=None):
    super().__init__(parent=parent)
    self.resize(800, 600)
    self.setStyleSheet("""#central_widget {
      background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,
      stop:0 rgba(87, 255, 140, 255), stop:1 rgba(117, 210, 255, 255));
    }""")
    self.centralwidget = QtWidgets.QWidget(self)
    self.centralwidget.setObjectName("central_widget")

    self.button = QtWidgets.QPushButton(self.centralwidget)
    self.button.setText("Hello World\n")
    self.button.clicked.connect(self.BtnOnClicked)
    self.button.setStyleSheet("""
      /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,
      stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));*/
      background-color: white;
      border-radius: 15px;
      border-style: solid;
      border-width: 4px;
      border-color: grey;
      font: 32pt "Ubuntu";
    """)

    self.setCentralWidget(self.centralwidget)

  def BtnOnClicked(self):
    print("Button pressed.")

app = None
window = None

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

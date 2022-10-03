import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGroupBox, QVBoxLayout

from integration import integrate_double_trap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        button = QPushButton("Посчитай!")
        button.setCheckable(True)
        # noinspection PyUnresolvedReferences
        button.clicked.connect(self.the_button_was_clicked)

        self.text = QLabel(self)
        self.text.setText('Нажми на кнопку и все посчитается!')

        layout = QVBoxLayout(self)

        layout.addWidget(self.text)
        layout.addWidget(button)

        self.box = QGroupBox(self)

        self.box.setLayout(layout)

        self.setCentralWidget(self.box)

    def the_button_was_clicked(self):
        self.text.setText(str(integrate_double_trap(.0001)))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

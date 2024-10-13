from AutoDatesetGeneratorWindow import AutoDatesetGeneratorWindow
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoDatesetGeneratorWindow()
    window.show()
    sys.exit(app.exec())
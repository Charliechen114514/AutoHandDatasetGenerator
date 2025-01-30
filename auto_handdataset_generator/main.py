import sys
from PySide6 import QtWidgets
from Ui.AutoDatesetGeneratorWindowUi.AutoDatesetGeneratorWindowUi \
    import AutoDatesetGeneratorWindow 
# Issuing for the global use of my classifier
from loguru import logger

if __name__ == "__main__":
    logger.trace("creating application")
    app = QtWidgets.QApplication(sys.argv)
    logger.trace("creating application done")
    logger.trace("initializing mainwindow")
    main_window = AutoDatesetGeneratorWindow()
    logger.trace("initializing done")
    logger.trace("application show")
    main_window.show()
    res = app.exec()
    main_window.finalize()
    sys.exit(res)
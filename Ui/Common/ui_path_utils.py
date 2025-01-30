from PySide6.QtWidgets import QWidget, QFileDialog

class UiUtils:
    @staticmethod
    def fetch_selected_dirent(parent: QWidget, caption: str, dirent = ".") -> str:
        return QFileDialog.getExistingDirectory(parent, caption, dirent)
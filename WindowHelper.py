class WindowClassHelper:
    @staticmethod
    def gain_qss_file_string(path: str):
        try:
            with open(path, 'r', encoding='UTF-8') as file:
                return [file.read(), True]
        except Exception as e:
            return [str(e), False]


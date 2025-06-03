from pathlib import Path

class PathDirectoryManager:
    def __init__(self, directory_name: str):
        self.directory_path = directory_name

    @property
    def directory_path(self):
        return self._directory_path

    @directory_path.setter
    def directory_path(self, value: str):
        self._directory_path = self.find_directory(value)

    @staticmethod
    def files_list_by_directory(directory_path: Path) -> list[Path]:
        return [file for file in directory_path.iterdir()]

    @staticmethod
    def find_directory(directory_name: str):
        abs_path = Path(__file__).resolve().parent.parent / "super_resolution" / directory_name
        if not abs_path.exists():
            raise FileNotFoundError(f"Directory {directory_name} not found")
        return abs_path

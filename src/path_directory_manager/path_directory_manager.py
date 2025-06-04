from pathlib import Path
class PathDirectoryManager:
    __slots__ = ("_path",)

    def __init__(self, directory_name: str):
        self.path = directory_name

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, value: str):
        self._path = self.find_directory(value)

    @staticmethod
    def files_list_by_directory(directory_path: Path) -> list[Path]:
        return list(directory_path.iterdir())

    @staticmethod
    def find_directory(directory_name: str) -> Path:
        try:
            base_path = Path(__file__).resolve().parent.parent
        except NameError:
            raise RuntimeError("__file__ is not defined")

        abs_path = base_path / "super_resolution" / directory_name
        if not abs_path.exists():
            raise FileNotFoundError(f"Directory '{directory_name}' not found at {abs_path}")
        return abs_path


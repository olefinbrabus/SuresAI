from pathlib import Path

from src.path_directory_manager.path_directory_manager import PathDirectoryManager
from src.super_resolution.base import super_resolution

def main():
    pdm = PathDirectoryManager(directory_name="dataset")
    # dataset_abspath = pdm.directory_path.absolute()
    dataset_list = pdm.files_list_by_directory(pdm.directory_path)

    pdm.directory_name = "low-resolution_photos"
    # low_photos_abspath = pdm.directory_path.absolute()
    low_photos_list = pdm.files_list_by_directory(pdm.directory_path)

    pdm.directory_name = "high-resolution_photos"
    high_photos_abspath = pdm.directory_path.absolute()

    if dataset_list:
        process_photos_with_sr(dataset_list, high_photos_abspath)
    if low_photos_list:
        process_photos_with_sr(low_photos_list, high_photos_abspath)
    else:
        raise FileNotFoundError()


def process_photos_with_sr(photos_list: list[Path], dst_filepath: Path) -> None:
    for photo_path in photos_list:
        dst_filepath_with_name = str(dst_filepath / photo_path.name)
        super_resolution_by_abspath(str(photo_path), dst_filepath_with_name)


def super_resolution_by_abspath(photo_abspath: str, dst_filepath: str) -> None:
    super_resolution(photo_abspath, dst_filepath)


if __name__ == '__main__':
    main()
from logical_models.file_manager import FileManager
from logical_models.menu import Menu
from models.file import File
from models.file_block import FileBlock
from models.linked_list import LinkedList

from utils.debugger import json_stringify


def main() -> None:
    # file = File(12, 16)
    # file.append(
    #     FileBlock("28"),
    #     FileBlock("5"),
    #     FileBlock("12"),
    #     FileBlock("13"),
    #     FileBlock("1"),
    #     FileBlock("4"),
    # )
    # file_manager = FileManager()
    # file_manager.read_file(0)
    # json_stringify(file_manager.files[0])
    # file.calculate_file_size()
    # print(file.size)
    menu = Menu()
    menu.show()


if __name__ == "__main__":
    main()

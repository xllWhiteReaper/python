from logical_models.menu import Menu
from models.file import File
from models.file_fragment import FileFragment
from models.linked_list import LinkedList

from utils.debugger import json_stringify


def main() -> None:
    file = File()
    file.file_fragments.append(FileFragment(1.5))
    file.file_fragments.append(FileFragment(2.5))
    file.file_fragments.append(FileFragment(4))
    file.calculate_file_size()
    print(file.size)
    # linked_list = LinkedList[FileFragment]()
    # linked_list.append(FileFragment(1.5))
    # linked_list.append(FileFragment(2.5))
    # linked_list.append(FileFragment(4))
    # json_stringify(linked_list)
    # menu = Menu()
    # menu.show()


if __name__ == "__main__":
    main()

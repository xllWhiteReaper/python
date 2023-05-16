from logical_models.menu import Menu
from models.linked_list import LinkedList


def main() -> None:
    linked_list = LinkedList[int]()
    linked_list.append(4)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(1)
    linked_list.remove(2)
    print(linked_list)
    # menu = Menu()
    # menu.show()


if __name__ == "__main__":
    main()

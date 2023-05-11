from utils.text_utils import print_centered_text,\
    print_separation, print_n_new_lines
    
from models.memory_manager import MemoryManager


class Menu:
    def __init__(self) -> None:
        selected_option = -1

    def show(self):
        print_centered_text("### Hello, welcome to the app ###")
        print_separation()
        print_n_new_lines(2)
        print("Please select one of the following")

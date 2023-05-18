import time
from utils.text_utils import print_centered_text, print_red,\
    print_separation, print_n_new_lines

from logical_models.file_manager import MEMORY_DATA_PATHS, FileManager
from logical_models.file_manager import FILE_DATA_PATHS

POSSIBLE_ANSWERS = [
    "-1", *[str(i + 1)
            for i in range(len(FILE_DATA_PATHS)*len(MEMORY_DATA_PATHS))]
]
ACTIONS = {
    "1": (0, 0, "best"),
}


class Menu:
    def __init__(self) -> None:
        self.file_manager = FileManager()

    def show(self):
        option: str = "-2"
        while option != "-1":
            print_centered_text(
                "### Hello, welcome to the FILE MANAGEMENT app ###")
            print_separation()
            print_n_new_lines(2)
            print("Please select the number of file to open")
            print("If you want to exit the program, please enter '-1'")

            option = input()

            if option not in POSSIBLE_ANSWERS:
                print_red(
                    f"Please enter only {','.join([answer for answer in POSSIBLE_ANSWERS])}")
                time.sleep(0.2)
                continue

            if option == "-1":
                break

            else:
                self.file_manager.queue_handler(*ACTIONS[option])
                time.sleep(0.2)

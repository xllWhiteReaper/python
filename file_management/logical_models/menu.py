import time
from utils.text_utils import print_centered_text, print_red,\
    print_separation, print_n_new_lines

from logical_models.file_manager import FileManager

POSSIBLE_ANSWERS = [
    "-1", *[str(i + 1) for i in range(6)]
]

ACTIONS = {
    "1": (0, "best"),
    "2": (0, "first"),
    "3": (0, "worst"),
    "4": (1, "best"),
    "5": (1, "first"),
    "6": (1, "worst"),
}


class Menu:
    def __init__(self) -> None:
        self.file_manager = FileManager()

    def show(self):
        option: str = "-2"
        while option != "-1":
            print_centered_text("### Hello, welcome to the app ###")
            print_separation()
            print_n_new_lines(2)
            print("Please select one of the following")
            print("1. Show memory management with best approach for the first list")
            print("2. Show memory management with first approach for the first list")
            print("3. Show memory management with worst approach for the first list")
            print("4. Show memory management with best approach for the second list")
            print("5. Show memory management with first approach for the second list")
            print("6. Show memory management with worst approach for the second list")
            print("-1. Exit the program")

            option = input()

            if option not in POSSIBLE_ANSWERS:
                print_red(
                    f"Please enter only {','.join([str(answer) for answer in POSSIBLE_ANSWERS])}")
                time.sleep(0.2)
                continue

            if option == "-1":
                break

            else:
                self.file_manager.queue_handler(*ACTIONS[option])
                time.sleep(0.2)

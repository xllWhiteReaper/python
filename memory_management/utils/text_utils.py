import shutil


def print_centered_text(text: str):
    print(text.center(shutil.get_terminal_size().columns))


def print_separation(char="_"):
    print(char*shutil.get_terminal_size().columns)


def print_n_new_lines(n: int = 1):
    for _ in range(n):
        print()

import shutil


def print_centered_text(text):
    print(text.center(shutil.get_terminal_size().columns))


def print_separation(char="_"):
    print(char*shutil.get_terminal_size().columns)


def print_n_new_lines(n=1):
    for i in range(n):
        print()

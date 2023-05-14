import shutil


def print_centered_text(text: str) -> None:
    print(text.center(shutil.get_terminal_size().columns))


def print_separation(char: str = "_") -> None:
    return None if len(char) != 1 else print(char*shutil.get_terminal_size().columns)


def print_n_new_lines(n: int = 1) -> None:
    for _ in range(n):
        print()

import shutil

RED = "\033[91m"
AQUA = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
WARNING = "\u26A0"


def print_centered_text(text: str) -> None:
    print(text.center(shutil.get_terminal_size().columns))


def print_separation(char: str = "_") -> None:
    return None if len(char) != 1 else print(char*shutil.get_terminal_size().columns)


def print_n_new_lines(n: int = 1) -> None:
    for _ in range(n):
        print()


def print_red(text: str) -> None:
    print(f"{RED}{text}{RESET}")


def print_aqua(text: str) -> None:
    print(f"{AQUA}{text}{RESET}")


def print_yellow(text: str) -> None:
    print(f"{YELLOW}{text}{RESET}")


def print_green(text: str) -> None:
    print(f"{GREEN}{text}{RESET}")


def print_magenta(text: str) -> None:
    print(f"{MAGENTA}{WARNING} {text}{RESET}")

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


def print_n_new_lines(n: int = 1) -> None:
    for _ in range(n):
        print()


def print_red(text: str) -> None:
    print(f"{RED}{text}{RESET}")


def print_green(text: str) -> None:
    print(f"{GREEN}{text}{RESET}")

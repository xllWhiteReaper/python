from typing import Any


def has_adequate_arguments(arguments_list: list[Any], *arg_types: Any) -> bool:
    for argument in arguments_list:
        if not isinstance(argument, arg_types):
            return False
    return True

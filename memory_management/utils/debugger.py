import json
from typing import Any
from utils.custom_serializer import CustomSerializer
from utils.text_utils import print_n_new_lines


def json_stringify(object: Any, indent: int = 2) -> None:
    print_n_new_lines(2)
    print(f"Object of type {type(object)}")
    # print(json.dumps(object, indent=indent))
    print(json.dumps(object, indent=indent, cls=CustomSerializer))
    print_n_new_lines(2)

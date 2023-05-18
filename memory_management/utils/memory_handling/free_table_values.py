from models.page_table import PageTable
from utils.from_decimal_to_hexadecimal import from_decimal_to_hexadecimal
from utils.text_utils import print_red


def free_table_values(memory_map: dict[str, PageTable | None], memory_indexes: list[int]) -> None:
    for key, page_table in memory_map.items():
        if page_table is not None:
            addresses = page_table.memory_addresses
            [
                print_red(
                    f"Memory freed for the Job with Id: {key} in memory address: {from_decimal_to_hexadecimal(str(x))}")
                for x in addresses if x in memory_indexes]
            new_addresses = [
                x for x in addresses if x not in memory_indexes]

            if len(new_addresses) == 0:
                memory_map[key] = None

            else:
                page_table = memory_map[key]
                if page_table is not None:
                    page_table.memory_addresses = new_addresses

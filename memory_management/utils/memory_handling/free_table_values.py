from models.page_table import PageTable


def free_table_values(memory_map: dict[str, PageTable | None], memory_indexes: list[int]) -> None:
    for key, page_table in memory_map.items():
        if page_table is not None:
            addresses = page_table.memory_addresses
            [
                print(f"Memory freed for the Job with Id: {key} in memory address: {x}") for x in addresses if x in memory_indexes]
            new_addresses = [
                x for x in addresses if x not in memory_indexes]

            if len(new_addresses) == 0:
                memory_map[key] = None

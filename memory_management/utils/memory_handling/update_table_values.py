from models.page_table import PageTable


def update_table_values(memory_map: dict[str, PageTable], memory_indexes: list[int]) -> None:
    for key, page_table in memory_map.items():
        addresses = page_table.memory_addresses
        for address in addresses:
            if address in memory_indexes:
                addresses.remove(address)
        if len(addresses) == 0:
            del memory_map[key]
        else:
            memory_map[key] = PageTable(page_table.job_id, addresses)

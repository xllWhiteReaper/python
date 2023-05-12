from models.page_table import PageTable
from utils.debugger import json_stringify


def free_table_values(memory_map: dict[str, PageTable | None], memory_indexes: list[int]) -> None:
    print("FREEING SPACE FROM TABLES")
    for key, page_table in memory_map.items():
      # WORKS
        # addresses = page_table.memory_addresses
        # for address in addresses:
        #     if address in memory_indexes:
        #         addresses.remove(address)
      # WORKS
        if page_table is not None:
            addresses = page_table.memory_addresses
            new_addresses = [
                x for x in addresses if x not in memory_indexes]
            print("new_addresses")
            json_stringify(new_addresses)

            # for address in addresses:
            #     if address in memory_indexes:
            #         addresses.remove(address)
            if len(new_addresses) == 0:
                print("memory_map[key] from freeing tables")
                json_stringify(memory_map[key])
                print(f"removing index {key}")
                # del memory_map[key]
                memory_map[key] = None

                # memory_map = {
                #     k: value for k, value in memory_map.items() if k is not key}
            # else:
            #     memory_map[key] = PageTable(page_table.job_id, new_addresses)

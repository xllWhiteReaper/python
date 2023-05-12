from models.job_fragment import JobFragment
from models.page_table import PageTable


def free_memory_space(queue_list: list[JobFragment | None], target_memory: int) -> int:
    # I will just use the first space that I find, because I might be
    # making it more complex than needed, IT COULD BE MADE EVEN MORE
    # EFFICIENTLY
    counter: int = 0
    index: int = -1
    possible_index: int = -1
    for idx, job_fragment in enumerate(queue_list):

        if job_fragment is None:
            counter += 1

            if counter == 1:
                possible_index = idx

            if counter == target_memory:
                index = possible_index
                break

        else:
            if job_fragment.current_state == "Sleep":
                counter += 1
                continue
            counter = 0
            possible_index = -1
            continue

    if index != -1:
        # Remove the table
        pass
    return index


def update_table_values(memory_map: dict[str, PageTable], memory_indexes: list[int]) -> None:
    for key, page_table in memory_map.items():
        addresses = page_table.memory_addresses
        for address in addresses:
            if address in memory_indexes:
                addresses.remove(address)
        if len(addresses) == 0:
            del memory_map[key]
        else:
            # new_page_table = PageTable(page_table.job_id, addresses)
            memory_map[key] = PageTable(page_table.job_id, addresses)
        pass
        # for address in table.memory_addresses:
        #     if address in indexes:
        #         ta
        #         pass
        # pass
    # check if there are empty lists for a table

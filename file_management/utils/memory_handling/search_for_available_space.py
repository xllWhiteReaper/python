from models.memory_fragment import MemoryFragment
from utils.searching_algorithms.search_for_best_location import search_for_best_location
from utils.searching_algorithms.search_for_first_location import search_for_first_location
from utils.searching_algorithms.search_for_worst_location import search_for_worst_location


def search_for_available_space(queue_list: list[MemoryFragment | None], queue_type: str, target_memory: int) -> int:
    if queue_type == "best":
        return search_for_best_location(queue_list, target_memory)
    elif queue_type == "first":
        return search_for_first_location(queue_list, target_memory)
    elif queue_type == "worst":
        return search_for_worst_location(queue_list, target_memory)
    else:
        return -1

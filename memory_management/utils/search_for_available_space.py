from models.job import Job
from utils.searching_algorithms.search_for_best_location import search_for_best_location
from utils.searching_algorithms.search_for_first_location import search_for_first_location
from utils.searching_algorithms.search_for_worst_location import search_for_worst_location


def search_for_available_space(queue_list: list[Job | None], queue_type: str, target_memory: int):
    if queue_type == "best":
        search_for_best_location(queue_list, target_memory)
    elif queue_type == "first":
        search_for_first_location(queue_list, target_memory)
    elif queue_type == "worst":
        search_for_worst_location(queue_list, target_memory)

from models.job import Job


def search_for_available_space(queue_list: list[Job | None], queue_type: str, target_memory: int):
    if queue_type == "best":
        search_for_best_location(queue_list, target_memory)
    elif queue_type == "first":
        search_for_best_location(queue_list, target_memory)
    elif queue_type == "worst":
        search_for_best_location(queue_list, target_memory)


def search_for_best_location(queue_list: list[Job | None], target_memory: int) -> int:
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
            counter = 0
            possible_index = -1
            continue
    return index


def search_for_first_location(queue_list: list[Job | None], target_memory: int):
    pass


def search_for_worst_location(queue_list: list[Job | None], target_memory: int):
    # at the middle of the biggest available space
    pass

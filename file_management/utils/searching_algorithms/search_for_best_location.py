from models.job_fragment import JobFragment


def search_for_best_location(queue_list: list[JobFragment | None], target_memory: int) -> int:
    queue_size = len(queue_list)
    counter: int = 0
    first_index: int = -1
    index: int = -1
    possible_index: int = -1
    for idx, job_fragment in enumerate(queue_list):

        if job_fragment is None:
            counter += 1

            if counter == 1:
                possible_index = idx

            if counter == target_memory and first_index == -1:
                first_index = possible_index

            if counter == target_memory and idx == (queue_size - 1):
                index = possible_index
                break

            if counter == target_memory and idx < (queue_size - 1) and queue_list[idx + 1] is not None:
                index = possible_index
                break

        else:
            counter = 0
            possible_index = -1
            continue
    if index == -1 and first_index != -1:
        # didn't find the most optimal index
        return first_index

    return index

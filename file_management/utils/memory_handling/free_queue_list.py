from models.job_fragment import JobFragment


def free_queue_list(queue_list: list[JobFragment | None],  memory_indexes: list[int]):
    for index in memory_indexes:
        queue_list[index] = None

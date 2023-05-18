from models.memory_fragment import MemoryFragment


def free_queue_list(queue_list: list[MemoryFragment | None],  memory_indexes: list[int]):
    for index in memory_indexes:
        queue_list[index] = None

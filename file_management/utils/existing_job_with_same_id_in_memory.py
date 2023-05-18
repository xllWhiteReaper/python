from models.memory_fragment import MemoryFragment


def existing_job_with_same_id_in_memory(queue_list: list[MemoryFragment | None], job_id: str) -> bool:
    # checks to see if there is a task in memory with the same id as the one we are
    # trying to add.
    # This is done by checking if there is any case where the fragments that are
    # in the que list have the same id as the new job
    return any([job.id == job_id for job in queue_list if job is not None])

from models.memory_fragment import MemoryFragment


def existing_job_with_same_id_in_memory(queue_list: list[MemoryFragment | None], job_id: str) -> bool:
    return any([job.id == job_id for job in queue_list if job is not None])

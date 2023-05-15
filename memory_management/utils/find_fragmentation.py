from models.job_fragment import JobFragment
from utils.text_utils import print_magenta


def find_fragmentation(jobs_list: list[JobFragment | None]) -> None:
    start_index = None
    for i, job in enumerate(jobs_list):
        if job is not None:
            if start_index is not None and i - start_index > 0:
                if start_index == i - 1:
                    print_magenta(f"Fragmentation at index {start_index}")
                else:
                    print_magenta(
                        f"Fragmentation between indexes {start_index} and {i-1}")
            start_index = None
        elif start_index is None:
            start_index = i

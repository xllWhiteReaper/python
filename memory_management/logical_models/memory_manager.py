import csv
import math

from models.job_fragment import JobFragment
from models.page_table import PageTable
from utils.find_fragmentation import find_fragmentation
from utils.from_decimal_to_hexadecimal import from_decimal_to_hexadecimal
from utils.memory_handling.deallocate_memory import deallocate_memory
from utils.memory_handling.free_memory_space import free_memory_space
from utils.memory_handling.search_for_available_space import search_for_available_space
from utils.existing_job_with_same_id_in_memory import existing_job_with_same_id_in_memory
from utils.text_utils import print_aqua, print_centered_text, print_green,\
    print_separation, print_n_new_lines, print_yellow
# from utils.debugger import json_stringify
from utils.time_manager import TimeManager

PAGE_SIZE = 1
REAL_EXECUTION_TIME = 0.01
TOTAL_MEMORY_SIZE = 20
NUMBER_OF_PAGES = math.floor(TOTAL_MEMORY_SIZE/PAGE_SIZE)
CHECKING_INTERVAL = 1
MEMORY_DATA_PATHS = [
    "./data/first_list.csv",
    "./data/second_list.csv"
]


class MemoryManager:
    def __init__(self) -> None:
        self.memory_data_list: list[list[JobFragment] | None] = [
            None for _ in MEMORY_DATA_PATHS]

        self.memory_maps: list[dict[str, (PageTable | None)]] = [
            {} for _ in MEMORY_DATA_PATHS]

    def get_jobs_from_file(self, file_name: str) -> list[JobFragment]:
        jobs: list[JobFragment] = []
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                id, start_time, required_size, execution_interval, state_after_interval = tuple(
                    row)
                jobs.append(JobFragment(id, start_time, required_size,
                            execution_interval, state_after_interval))
        return jobs

    def get_jobs_from_n_list(self, n: int) -> None:
        try:
            URL = MEMORY_DATA_PATHS[n]
            self.memory_data_list[n] = self.get_jobs_from_file(URL)
        except:
            return

    def show_os_simulation(self, list_number: int = 0) -> None:
        self.queue_with_specific_fit_approach(list_number, "best")

    def queue_with_specific_fit_approach(self, list_number: int, queue_type: str) -> None:
        time_manager = TimeManager()
        print_n_new_lines(2)
        print_centered_text(
            f"{queue_type.title()} Fit Queue for list {list_number + 1}")
        print_n_new_lines()
        print(f"Started the process of queuing")
        print_n_new_lines()
        queue_list: list[None | JobFragment] = [
            None for _ in range(NUMBER_OF_PAGES)]
        jobs_list = self.memory_data_list[list_number]

        if jobs_list is not None:
            while len(jobs_list) > 0 or self.jobs_still_running(queue_list):
                print_separation()
                jobs_list = self.memory_data_list[list_number]
                job_to_add: JobFragment | None
                next_memory_address = -1
                if jobs_list is not None and len(jobs_list) > 0:
                    job_to_add = jobs_list[0]
                else:
                    job_to_add = None
                allocation_size = TOTAL_MEMORY_SIZE + 1
                if job_to_add is not None:
                    allocation_size = int(math.floor(
                        int(job_to_add.required_size))/2)

                    # check if it is already in the list
                    already_in_list = existing_job_with_same_id_in_memory(
                        queue_list, allocation_size, job_to_add.id)

                    if (already_in_list):
                        deallocate_memory(
                            queue_list, self.memory_maps[list_number], job_to_add.id)

                    next_memory_address = search_for_available_space(
                        queue_list, queue_type, allocation_size)

                if next_memory_address == -1 and jobs_list is not None:
                    next_memory_address, pending_jobs = free_memory_space(
                        queue_list, self.memory_maps[list_number], allocation_size)
                    [jobs_list.append(job) for job in pending_jobs]
                    self.check_memory_maps(list_number)

                if next_memory_address > -1 and job_to_add is not None and jobs_list is not None:
                    self.allocate_job_in_memory(queue_list, time_manager.get_elapsed_time(
                    ), list_number, next_memory_address, job_to_add)
                    jobs_list.pop(0)

                self.check_jobs_in_memory_status(
                    queue_list, time_manager.get_elapsed_time(), list_number)

                find_fragmentation(queue_list)

                time_manager.sleep(CHECKING_INTERVAL)

            print_n_new_lines(2)
            print_green("All jobs finished their execution!")

    def jobs_still_running(self, queue_list: list[JobFragment | None]) -> bool:
        return True if any([job.current_state == "Running" for job in queue_list if job is not None]) else False

    def check_memory_maps(self, list_number: int):
        self.memory_maps[list_number] = {
            key: value for key, value in self.memory_maps[list_number].items() if value is not None}

    def queue_handler(self, list_number: int, queue_type: str):
        try:
            self.get_jobs_from_n_list(list_number)
            self.queue_with_specific_fit_approach(list_number, queue_type)
        except:
            return

    def check_jobs_in_memory_status(self, queue_list: list[JobFragment | None], elapsed_time: float, list_number: int) -> None:
        found_job_id: str = "-1"
        for queued_job in queue_list:
            if queued_job is not None and queued_job.id != found_job_id:
                try:
                    if elapsed_time >= int(queued_job.start_time) and queued_job.current_state == "Pending":
                        # Add color green
                        print_aqua(
                            f"Job with id {queued_job.id} has started running")
                        queued_job.current_state = "Running"
                    # Supposing that the csv schema is adequate and every task will start its
                    # execution at the estated time
                    elif elapsed_time >= int(queued_job.start_time) + int(queued_job.execution_interval):
                        print_green(
                            f"Job with id {queued_job.id} has finished its execution interval")
                        queued_job.current_state = queued_job.state_after_interval

                    found_job_id = queued_job.id
                except:
                    return

                if queued_job.current_state == "End":
                    deallocate_memory(
                        queue_list, self.memory_maps[list_number], queued_job.id)

                if queued_job.current_state == "Sleep":
                    print_yellow(
                        f"Job with id {queued_job.id} is sleeping")

                if queued_job.current_state == "Running":
                    print_aqua(
                        f"Job with id {queued_job.id} is running")

    def allocate_job_in_memory(self, queue_list: list[JobFragment | None], elapsed_time: float, list_number: int, start_index: int, job_to_add: JobFragment):
        # we will consider that the indexes of allocation are continuos
        try:
            allocation_size = int(math.floor(int(job_to_add.required_size))/2)
        except:
            return
        # setting new start time for job that didn't start at the expected time
        if int(job_to_add.start_time) < elapsed_time:
            job_to_add.start_time = f"{int(round(elapsed_time))}"
        # setting the memory fragments into memory
        index_range = start_index, start_index + allocation_size
        for i in range(*index_range):
            queue_list[i] = job_to_add
            # simulates that it is a hexadecimal location
            print_yellow(
                f"Job with Id: {job_to_add.id} has been allocated to memory in address: {from_decimal_to_hexadecimal(str(i))}")

        # adding new addresses to the address tables
        self.memory_maps[list_number][job_to_add.id] = PageTable(
            job_to_add.id,  [i for i in range(*index_range)])

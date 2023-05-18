import csv
import math
from models.file import File
from models.file_block import FileBlock

from models.memory_fragment import MemoryFragment
from models.page_table import PageTable
from utils.find_fragmentation import find_fragmentation
from utils.float_to_int import float_to_int
from utils.from_decimal_to_hexadecimal import from_decimal_to_hexadecimal
from utils.memory_handling.deallocate_memory import deallocate_memory
from utils.memory_handling.free_memory_space import free_memory_space
from utils.memory_handling.search_for_available_space import search_for_available_space
from utils.existing_job_with_same_id_in_memory import existing_job_with_same_id_in_memory
from utils.searching_algorithms.search_for_page_indexes import search_for_page_indexes
from utils.text_utils import print_aqua, print_centered_text, print_green,\
    print_separation, print_n_new_lines, print_yellow
# from utils.debugger import json_stringify
from utils.time_manager import TimeManager

DISK_BLOCK_SIZE = 1
PAGE_SIZE = 1
REAL_EXECUTION_TIME = 0.01
TOTAL_MEMORY_SIZE = 20
NUMBER_OF_PAGES = math.floor(TOTAL_MEMORY_SIZE/PAGE_SIZE)
CHECKING_INTERVAL = 1
MEMORY_DATA_PATHS = [
    "./data/first_list.csv",
]
FILE_DATA_PATHS = [
    "./data/file1.csv",
]


class FileManager:
    def __init__(self) -> None:
        self.memory_data_list: list[list[MemoryFragment] | None] = [
            None for _ in MEMORY_DATA_PATHS]

        self.memory_maps: list[dict[str, (PageTable | None)]] = [
            {} for _ in MEMORY_DATA_PATHS]

        self.files: list[File] = [File() for _ in FILE_DATA_PATHS]

    def get_jobs_from_file(self, file_name: str) -> list[MemoryFragment]:
        jobs: list[MemoryFragment] = []
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                id, start_time, required_size, execution_interval, state_after_interval = tuple(
                    row)
                jobs.append(MemoryFragment(id, start_time, required_size,
                            execution_interval, state_after_interval))
        return jobs

    def get_jobs_from_n_list(self, n: int) -> None:
        try:
            URL = MEMORY_DATA_PATHS[n]
            self.memory_data_list[n] = self.get_jobs_from_file(URL)
        except:
            return

    def queue_with_specific_fit_approach(self, file_number: int, list_number: int, queue_type: str) -> None:
        time_manager = TimeManager()
        print_n_new_lines(2)
        print_centered_text(
            f"{queue_type.title()} Fit Queue for list {list_number + 1}")
        print_n_new_lines()
        print(f"Started the process of queuing")
        print_n_new_lines()
        queue_list: list[None | MemoryFragment] = [
            None for _ in range(NUMBER_OF_PAGES)]
        jobs_list = self.memory_data_list[list_number]

        # FILE RELATED STUFF
        already_loaded_file_to_memory = False
        # read the file information
        self.read_file(file_number)
        file: File = self.files[file_number]
        # FILE RELATED STUFF

        if jobs_list is not None:
            while len(jobs_list) > 0 or self.jobs_still_running(queue_list):
                print_separation()
                jobs_list = self.memory_data_list[list_number]
                job_to_add: MemoryFragment | None
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
                        queue_list, job_to_add.id)

                    if (already_in_list):
                        deallocate_memory(
                            queue_list, self.memory_maps[list_number], job_to_add.id)

                    # searches for memory addresses that are available
                    next_memory_address = search_for_available_space(
                        queue_list, queue_type, allocation_size)

                if next_memory_address == -1 and jobs_list is not None:
                    # deallocate if didn't find a block
                    next_memory_address, pending_jobs = free_memory_space(
                        queue_list, self.memory_maps[list_number], allocation_size)
                    [jobs_list.append(job) for job in pending_jobs]
                    self.check_memory_maps(list_number)

                if next_memory_address > -1 and job_to_add is not None and jobs_list is not None:
                    # allocates if there is enough space and running task aren't thrown away
                    self.allocate_job_in_memory(queue_list, time_manager.get_elapsed_time(
                    ), list_number, next_memory_address, job_to_add)
                    jobs_list.pop(0)

                # ALLOCATING THE FILE INTO MEMORY
                if file.allocation_time <= time_manager.get_elapsed_time() and not already_loaded_file_to_memory:
                    self.show_allocation_for_file(
                        file_number,
                        list_number,
                        time_manager.get_elapsed_time(),
                        queue_list,
                    )
                    already_loaded_file_to_memory = True

                self.check_jobs_in_memory_status(
                    queue_list, time_manager.get_elapsed_time(), list_number)

                find_fragmentation(queue_list)

                time_manager.sleep(CHECKING_INTERVAL)

            print_n_new_lines(2)
            print_green("All jobs finished their execution!")

    def jobs_still_running(self, queue_list: list[MemoryFragment | None]) -> bool:
        return True if any([job.current_state == "Running" for job in queue_list if job is not None]) else False

    def check_memory_maps(self, list_number: int):
        self.memory_maps[list_number] = {
            key: value for key, value in self.memory_maps[list_number].items() if value is not None}

    def queue_handler(self, file_number: int, list_number: int, queue_type: str):
        try:
            self.get_jobs_from_n_list(list_number)
            self.queue_with_specific_fit_approach(
                file_number, list_number, queue_type)
        except:
            return

    def read_file(self, file_number: int) -> None:
        if file_number >= len(FILE_DATA_PATHS):
            return
        file_name = FILE_DATA_PATHS[file_number]
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            memory_blocks_string, allocation_time, deallocation_time = tuple(
                next(csv_reader))
            try:
                # to refresh the file if the user makes another petition
                self.files[file_number] = File()
                self.files[file_number].allocation_time = float(
                    allocation_time)
                self.files[file_number].deallocation_time = float(
                    deallocation_time)
                # this is the form to separate the memory block ids just because of the way
                # the csv is saved
                self.files[file_number].append(
                    *[FileBlock(meta_data) for meta_data in memory_blocks_string.split("-")])
            except:
                return

    def show_allocation_for_file(
        self,
        file_number: int,
        list_number: int,
        elapsed_time: float,
        queue_list: list[None | MemoryFragment]
    ) -> None:
        # creation of new memory fragments from file fragments
        head = self.files[file_number].file_fragments.head
        memory_fragment: MemoryFragment
        allocation_size: int = math.ceil(self.files[file_number].size)
        already_in_list = False
        if head is not None:
            memory_fragment = MemoryFragment(
                head.data.metadata,
                str(float_to_int(self.files[file_number].allocation_time)),
                str(allocation_size),
                str(float_to_int(self.files[file_number].deallocation_time -
                                 self.files[list_number].allocation_time)),
                "End"
            )
            # check if it is already in the list
            already_in_list = existing_job_with_same_id_in_memory(
                queue_list, memory_fragment.id)

            if (already_in_list):
                deallocate_memory(
                    queue_list, self.memory_maps[list_number], memory_fragment.id)

        memory_map = self.memory_maps[list_number]

        allocation_indexes, pending_memory_fragments = search_for_page_indexes(
            queue_list, memory_map, allocation_size)

        if len(allocation_indexes) < allocation_size:
            print(
                "The file that you tried to open couldn't be loaded into the the memory because there are jobs with higher priority executing, consider getting more RAM or more virtual memory")
            return

        if memory_fragment is not None:
            self.allocate_file_in_memory(
                queue_list, list_number, elapsed_time, allocation_indexes, memory_fragment)

        jobs_list = self.memory_data_list[list_number]
        if jobs_list is not None:
            jobs_list = [*jobs_list, *pending_memory_fragments]

        self.check_memory_maps(list_number)

    def check_jobs_in_memory_status(self, queue_list: list[MemoryFragment | None], elapsed_time: float, list_number: int) -> None:
        # logs into the console the statuses of the jobs, and also sets some depending on the condition
        found_job_id: str = "-1"
        for queued_job in queue_list:
            if queued_job is not None and queued_job.id != found_job_id:
                try:
                    if elapsed_time >= int(queued_job.start_time) and queued_job.current_state == "Pending":
                        print_aqua(
                            f"Job with id {queued_job.id} has started running")
                        queued_job.current_state = "Running"
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

    def allocate_job_in_memory(self, queue_list: list[MemoryFragment | None], elapsed_time: float, list_number: int, start_index: int, job_to_add: MemoryFragment):
        try:
            allocation_size = int(math.floor(int(job_to_add.required_size))/2)
        except:
            return
        # setting new start time for job that didn't start at the expected time
        if int(job_to_add.start_time) < elapsed_time:
            job_to_add.start_time = f"{float_to_int(elapsed_time)}"
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

    def allocate_file_in_memory(
        self,
        queue_list: list[MemoryFragment | None],
        list_number: int,
        elapsed_time: float,
        indexes: list[int],
        file_to_add: MemoryFragment
    ):
        # setting new start time for job that didn't start at the expected time
        if int(file_to_add.start_time) < elapsed_time:
            file_to_add.start_time = f"{float_to_int(elapsed_time)}"
        for index in indexes:
            queue_list[index] = file_to_add
            # simulates that it is a hexadecimal location
            print_yellow(
                f"File with Id: {file_to_add.id} has been allocated to memory in address: {from_decimal_to_hexadecimal(str(index))}")
        # adding new addresses to the address tables
        self.memory_maps[list_number][file_to_add.id] = PageTable(
            file_to_add.id,  indexes)

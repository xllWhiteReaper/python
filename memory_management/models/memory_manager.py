import csv
import math

from models.job_fragment import JobFragment
from models.page_table import PageTable
from utils.memory_handling.deallocate_memory import deallocate_memory
from utils.memory_handling.free_table_values import free_table_values
from utils.memory_handling.free_queue_list import free_queue_list
from utils.memory_handling.free_memory_space import free_memory_space
# from utils.search_for_available_space import search_for_available_space
from utils.text_utils import print_centered_text,\
    print_separation, print_n_new_lines
from utils.debugger import json_stringify
from utils.time_manager import TimeManager

PAGE_SIZE = 1
REAL_EXECUTION_TIME = 0.01
TOTAL_MEMORY_SIZE = 20
NUMBER_OF_PAGES = math.floor(TOTAL_MEMORY_SIZE/PAGE_SIZE)
CHECKING_INTERVAL = 3
MEMORY_DATA_PATHS = [
    "./first_list.csv",
    "./second_list.csv"
]


class MemoryManager:
    def __init__(self) -> None:
        self.page_tables = []
        self.memory_data_list = [None for _ in MEMORY_DATA_PATHS]

        self.memory_maps: list[dict[str, (PageTable | None)]] = [{
            "2": PageTable("2",  [0, 2, 3, 5]),
            "3": PageTable("3",  [6, 8, 10]),
            "4": PageTable("4",  [12, 14, 16, 18]),
        }]

    def get_jobs_from_file(self, file_name):
        print("GETTING JOBS FROM FILE")
        jobs = []
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                id, start_time, required_size, execution_interval, state_after_interval = tuple(
                    row)
                jobs.append(JobFragment(id, start_time, required_size,
                            execution_interval, state_after_interval))
        print("After file opening")
        return jobs

    def get_jobs_from_n_list(self, n):
        try:
            print("Trying", n)
            URL = MEMORY_DATA_PATHS[n]
            self.memory_data_list[n] = self.get_jobs_from_file(URL)
            print("json_stringify(job)")
            # json_stringify(self.memory_data_list[n])
            job = JobFragment("1", "1", "1", "1", "1")
            # json_stringify(job)
            # json_stringify(
            #     [PageTable(1), "", {"key": "value"}, None, None, None, job])
            # [PageTable(1)])
        except:
            print("EXCEPTION")
            return

    def show_os_simulation(self):
        pass

    def add_to_queue(queue_list, job, queue_type):
        if queue_type == "best":
            pass
        elif queue_type == "first":
            pass
        elif queue_type == "worst":
            pass

    def queue_best_fit_approach(self, list_number: int):
        time_manager = TimeManager()
        print_n_new_lines(2)
        print_centered_text("Best Fit Queue")
        print_n_new_lines()
        print(f"Started the process of queuing")
        print_n_new_lines()
        queue_list: list[None | JobFragment] = [
            None for _ in range(NUMBER_OF_PAGES)]
        # for i in range(NUMBER_OF_PAGES):
        #     if i % 2 == 0:
        #         queue_list[i] = Job("2", "1", "4", "3", "Sleep")
        job_to_add = JobFragment("5", "1", "6", "3", "Sleep")
        allocation_size = int(math.floor(int(job_to_add.required_size))/2)

        queue_list[0] = JobFragment("2", "1", "4", "3", "Sleep")
        # queue_list[0].current_state = "Running"
        # queue_list[2] = JobFragment("2", "1", "4", "3", "Sleep")
        # queue_list[2].current_state = "Running"
        # queue_list[3] = JobFragment("2", "1", "4", "3", "Sleep")
        # queue_list[3].current_state = "Running"
        # queue_list[4] = JobFragment("2", "1", "4", "3", "Sleep")
        # queue_list[4].current_state = "Running"
        # queue_list[5] = JobFragment("2", "1", "4", "3", "Sleep")
        # queue_list[5].current_state = "Pending"

        queue_list[6] = JobFragment("3", "1", "4", "3", "Running")
        # queue_list[6].current_state = "Pending"

        # queue_list[7] = JobFragment("5", "1", "8", "3", "Running")
        # queue_list[7].current_state = "Pending"

        # queue_list[8] = JobFragment("3", "1", "4", "3", "Running")
        # queue_list[10] = JobFragment("3", "1", "4", "3", "Running")

        # queue_list[12] = JobFragment("4", "1", "4", "3", "Sleep")
        # queue_list[14] = JobFragment("4", "1", "4", "3", "Sleep")
        # queue_list[16] = JobFragment("4", "1", "4", "3", "Sleep")
        # queue_list[18] = JobFragment("4", "1", "4", "3", "Sleep")
        print("Before allocating memory")
        print("queue_list")
        json_stringify(queue_list)
        print("self.memory_maps[list_number]")
        json_stringify(self.memory_maps[list_number])

        self.allocate_job_in_memory(queue_list, 8.51, 0, 1, job_to_add)
        print_separation()
        print("After allocating memory")
        print("queue_list")
        json_stringify(queue_list)
        print("self.memory_maps[list_number]")
        json_stringify(self.memory_maps[list_number])

        # print("BEFORE FREEING MEMORY SPACE")
        # print("queue_list")
        # json_stringify(queue_list)
        # # print(queue_list)
        # print("self.memory_maps")
        # json_stringify(self.memory_maps)
        # print_separation()
        # print("AFTER FREEING MEMORY SPACE")
        # print("ok")
        # specific_list_table = self.memory_maps[list_number]
        # # specific_list_table: PageTable = self.memory_maps[jobs_list]
        # # free_table_values(
        # #     specific_list_table, [0, 2, 3, 5, 8, 14])
        # print(free_memory_space(queue_list, specific_list_table, 3))
        # # free_queue_list(queue_list, [0, 2, 3])
        # # JUST ERASES THE FIRST ITEM IN THE LIST
        # self.check_memory_maps(list_number)

        # print("self.memory_maps")
        # json_stringify(self.memory_maps)

        # print("queue_list")
        # json_stringify(queue_list)
        # print("self.memory_maps")
        # json_stringify(self.memory_maps)

        # jobs_list_copy = jobs_list[::]
        # print("Searching for worst location")
        # print(f"Index: {search_for_worst_location(queue_list, 2)}")
        # for job in jobs_list_copy:
        # print("checking jobs")
        # while time_manager.get_elapsed_time() < 10:
        #     print_separation()
        #     print(f"inside for loop")
        #     # print(
        #     #     f"Time since the start of the function: {curr_time()-start_time}")
        #     # print("jobs_list")
        #     # self.test()
        #     self.check_jobs_in_memory_status(
        #         queue_list, time_manager.get_elapsed_time())
        #     time_manager.sleep(CHECKING_INTERVAL)
        #     # print(job)
        # # while awaiting_jobs:
        # #     for job in jobs_list:
        # #         if job.current_state == "Pending":
        # #             pass
        # #         pass
        # print(queue_list)
    def check_memory_maps(self, list_number: int):
        self.memory_maps[list_number] = {
            key: value for key, value in self.memory_maps[list_number].items() if value is not None}

    def queue_first_fit_approach(self, jobs_list):
        pass

    def queue_worst_fit_approach(self, jobs_list):
        pass

    def queue_handler(self, list_number: int, queue_type: str):
        try:
            # job_list = self.memory_data_list[list_number]
            if queue_type == "best":
                self.queue_best_fit_approach(list_number)
            elif queue_type == "first":
                self.queue_first_fit_approach(list_number)
            elif queue_type == "worst":
                self.queue_worst_fit_approach(list_number)
        except:
            return

    def check_jobs_in_memory_status(self, queue_list: list[JobFragment | None], elapsed_time: float) -> None:
        found_job_id: str = "-1"
        for queued_job in queue_list:
            if queued_job is not None and queued_job.id != found_job_id:
                try:
                    if elapsed_time >= int(queued_job.start_time) and queued_job.current_state == "Pending":
                        # Add color green
                        print(
                            f"Job with id {queued_job.id} has started running")
                        queued_job.current_state = "Running"
                    # Supposing that the csv schema is adequate and every task will start its
                    # execution at the estated time
                    elif elapsed_time >= int(queued_job.start_time) + int(queued_job.execution_interval):
                        print(
                            f"Job with id {queued_job.id} has finished its execution interval")
                        queued_job.current_state = queued_job.state_after_interval

                    found_job_id = queued_job.id
                except:
                    return

                if queued_job.current_state == "End":
                    deallocate_memory(
                        queue_list, self.memory_map, queued_job.id)

                if queued_job.current_state == "Sleep":
                    print(
                        f"Job with id {queued_job.id} is sleeping")

    def allocate_job_in_memory(self, queue_list: list[JobFragment | None], elapsed_time: float, list_number: int, start_index: int, job_to_add: JobFragment):
        # we will consider that the indexes of allocation are continuos
        try:
            allocation_size = int(math.floor(int(job_to_add.required_size))/2)
            print(f"Space to be allocated: {allocation_size}")
            # print(f"rounded elapsed time {int(round(elapsed_time))}")
        except:
            return
        # setting new start time for job that didn't start at the expected time
        if int(job_to_add.start_time) < elapsed_time:
            job_to_add.start_time = f"{int(round(elapsed_time))}"
        # setting the memory fragments into memory
        index_range = start_index, start_index + allocation_size
        for i in range(*index_range):
            queue_list[i] = job_to_add
        # adding new addresses to the address tables
        self.memory_maps[list_number][job_to_add.id] = PageTable(
            job_to_add.id,  [i for i in range(*index_range)])

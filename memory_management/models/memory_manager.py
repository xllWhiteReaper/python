from ast import Dict
import csv
import math
import time

from typing import Union
from models.job import Job
from models.page_table import PageTable
from utils.deallocate_memory import deallocate_memory
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

        self.memory_map: dict[str, PageTable] = {
            "2": PageTable("2",  [0, 1, 2, 3])
        }

    def get_jobs_from_file(self, file_name):
        print("GETTING JOBS FROM FILE")
        jobs = []
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                id, start_time, required_size, execution_interval, state_after_interval = tuple(
                    row)
                jobs.append(Job(id, start_time, required_size,
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
            job = Job("1", "1", "1", "1", "1")
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

    def queue_best_fit_approach(self, jobs_list):
        time_manager = TimeManager()
        print_n_new_lines(2)
        print_centered_text("Best Fit Queue")
        print_n_new_lines()
        print(f"Started the process of queuing")
        print_n_new_lines()
        queue_list = [None for _ in range(NUMBER_OF_PAGES)]
        queue_list[0] = Job("2", "1", "4", "3", "Sleep")
        # queue_list[1] = Job("2", "1", "4", "3", "End")
        # queue_list[2] = Job("2", "1", "4", "3", "End")
        # queue_list[3] = Job("2", "1", "4", "3", "End")
        # queue_list[4] = Job("2", "1", "4", "3", "End")
        jobs_list_copy = jobs_list[::]
        # for job in jobs_list_copy:
        print("checking jobs")
        while time_manager.get_elapsed_time() < 10:
            print_separation()
            print(f"inside for loop")
            # print(
            #     f"Time since the start of the function: {curr_time()-start_time}")
            # print("jobs_list")
            # self.test()
            self.check_jobs_in_memory_status(
                queue_list, time_manager.get_elapsed_time())
            time_manager.sleep(CHECKING_INTERVAL)
            # print(job)
        # while awaiting_jobs:
        #     for job in jobs_list:
        #         if job.current_state == "Pending":
        #             pass
        #         pass
        print(queue_list)

    def test(self):
        print("HAHA")

    def queue_first_fit_approach(self, jobs_list):
        pass

    def queue_worst_fit_approach(self, jobs_list):
        pass

    def queue_handler(self, list_number, queue_type):
        try:
            job_list = self.memory_data_list[list_number]
            if queue_type == "best":
                self.queue_best_fit_approach(job_list)
            elif queue_type == "first":
                self.queue_first_fit_approach(job_list)
            elif queue_type == "worst":
                self.queue_worst_fit_approach(job_list)
        except:
            return

    def check_jobs_in_memory_status(self, queue_list: list[Job | None], elapsed_time: float) -> None:
        print("CHECKING JOBS INSIDE FUNCTION")
        for queued_job in queue_list:
            if queued_job is not None:
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
                except:
                    return

                if queued_job.current_state == "End":
                    deallocate_memory(
                        queue_list, self.memory_map, queued_job.id)

                if queued_job.current_state == "Sleep":
                    print(
                        f"Job with id {queued_job.id} is sleeping")

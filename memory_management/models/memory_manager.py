import csv
import time

from typing import Union
from models.job import Job
from models.page_table import PageTable
from utils.text_utils import print_centered_text,\
    print_separation, print_n_new_lines
from utils.debugger import json_stringify
from utils.time_manager import TimeManager

PAGE_SIZE = 1
REAL_EXECUTION_TIME = 0.01
TOTAL_MEMORY_SIZE = 20
CHECKING_INTERVAL = 3
MEMORY_DATA_PATHS = [
    "./first_list.csv",
    "./second_list.csv"
]


class MemoryManager:
    def __init__(self) -> None:
        self.page_tables = []
        self.memory_data_list = [None for _ in MEMORY_DATA_PATHS]

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
        queue_list = [None for _ in range(TOTAL_MEMORY_SIZE)]
        queue_list[0] = Job("2", "1", "4", "3", "End")
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

    def check_jobs_in_memory_status(self, queue_list: list[Union[Job, None]], elapsed_time: float) -> None:
        print("CHECKING JOBS INSIDE FUNCTION")
        for queued_job in queue_list:
            if queued_job is not None:
                print(f"elapsed: {elapsed_time}")
                print("stringify")
                json_stringify(queued_job)
                try:
                    if elapsed_time >= int(queued_job.start_time) and queued_job.current_state == "Pending":
                        print(
                            f"Job with id {queued_job.id} has started running")
                except:
                    return
            #         queued_job.current_state = "Running"

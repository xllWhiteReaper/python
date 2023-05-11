import time


class TimeManager:
    def __init__(self) -> None:
        self.curr_time = time.time
        self.start_time: float = self.curr_time()

    def start(self) -> None:
        self.start_time = self.curr_time()

    def restart(self) -> None:
        self.start_time = self.curr_time()

    def get_elapsed_time(self) -> float:
        return self.curr_time()-self.start_time

    def sleep(self, sleep_interval: float) -> None:
        time.sleep(sleep_interval)

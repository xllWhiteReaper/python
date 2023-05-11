class Job:
    def __init__(self,
                 id,
                 start_time,
                 required_size,
                 execution_interval,
                 state_after_interval) -> None:
        self.id = id
        self.start_time = start_time
        self.required_size = required_size
        self.execution_interval = execution_interval
        self.state_after_interval = state_after_interval
        self.current_state = "Pending"

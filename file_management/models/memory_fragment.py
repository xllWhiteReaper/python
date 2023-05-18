class MemoryFragment:
    def __init__(self,
                 id: str,
                 start_time: str,
                 required_size: str,
                 execution_interval: str,
                 state_after_interval: str) -> None:
        self.id = id
        self.start_time = start_time
        self.required_size = required_size
        self.execution_interval = execution_interval
        self.state_after_interval = state_after_interval
        self.current_state: str = "Pending"

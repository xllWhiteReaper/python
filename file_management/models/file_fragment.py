import random


class FileFragment:
    def __init__(self, size: float) -> None:
        self.size = size
        self.metadata = ""
        self.metadata_size = random.uniform(1, 10)

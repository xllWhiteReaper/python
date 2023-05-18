import random

DISK_BLOCK_SIZE = 1


class FileBlock:
    def __init__(self, metadata: str) -> None:
        self.size = DISK_BLOCK_SIZE
        self.metadata = metadata
        self.metadata_size = random.uniform(1, 10)

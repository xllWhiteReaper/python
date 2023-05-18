class PageTable:
    def __init__(self, job_id: str, addresses: list[int]) -> None:
        self.memory_addresses: list[int] = []
        self.job_id = job_id
        self.add_addresses(addresses)

    def add_addresses(self, addresses: list[int]):
        for address in addresses:
            self.memory_addresses.append(address)

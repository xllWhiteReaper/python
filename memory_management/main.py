from logical_models.menu import Menu, MemoryManager


def main() -> None:
    print("In main")
    memory_manager = MemoryManager()
    # menu = Menu()
    # menu.show()
    memory_manager.get_jobs_from_n_list(0)
    memory_manager.queue_handler(0, "best")


if __name__ == "__main__":
    main()

from ui.console_interface import ConsoleInterface
from services.allocation_service import AllocationService
from services.reallocation_service import ReallocationService
from services.metrics_service import MetricsService
from utils.data_storage import DataStorage
from utils.logger import Logger

def main():
    # Initialize services
    allocation_service = AllocationService()
    reallocation_service = ReallocationService()
    metrics_service = MetricsService()

    # Initialize utilities
    data_storage = DataStorage()
    logger = Logger()

    # Pass all components to the ConsoleInterface
    console_interface = ConsoleInterface(
        allocation_service,
        reallocation_service,
        metrics_service,
        data_storage,
        logger
    )

    # Start the console interface
    console_interface.run()

if __name__ == "__main__":
    main()



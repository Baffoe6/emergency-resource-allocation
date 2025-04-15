from ui.console_interface import ConsoleInterface
from services.allocation_service import AllocationService
from services.reallocation_service import ReallocationService
from services.metrics_service import MetricsService
from utils.data_storage import DataStorage
from utils.logger import Logger

def initialize_services():
    """Initialize and return all services."""
    return {
        'allocation_service': AllocationService(),
        'reallocation_service': ReallocationService(),
        'metrics_service': MetricsService()
    }

def initialize_utilities():
    """Initialize and return all utilities."""
    return {
        'data_storage': DataStorage(),
        'logger': Logger()
    }

def main():
    # Initialize services and utilities
    services = initialize_services()
    utilities = initialize_utilities()

    # Pass all components to the ConsoleInterface
    console_interface = ConsoleInterface(
        services['allocation_service'],
        services['reallocation_service'],
        services['metrics_service'],
        utilities['data_storage'],
        utilities['logger']
    )

    # Start the console interface
    console_interface.run()

if __name__ == "__main__":
    main()

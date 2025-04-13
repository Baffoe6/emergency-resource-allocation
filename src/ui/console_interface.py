from models.user import User

class ConsoleInterface:
    def __init__(self, allocation_service, reallocation_service, metrics_service, data_storage, logger):
        self.allocation_service = allocation_service
        self.reallocation_service = reallocation_service
        self.metrics_service = metrics_service
        self.data_storage = data_storage
        self.logger = logger
        self.incidents = []  # List to store incidents
        self.resources = []  # List to store resources
        self.users = []  # List to store users
        self.current_user = None  # Track the currently logged-in user

    def run(self):
        self.setup_users()  # Initialize default users
        self.authenticate_user()  # Authenticate the user before showing the menu

        # Load historical data at the start of the program
        self.load_historical_data()

        while True:
            print(f"\nWelcome, {self.current_user.username} ({self.current_user.role})!")
            print("Please select an option:")
            print("1. Log a new incident")
            print("2. Add a new resource")
            print("3. View incidents")
            print("4. View resources")
            print("5. Allocate resources")
            print("6. View resource utilization metrics")
            print("7. View historical data")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.log_incident()
            elif choice == "2":
                self.add_resource()
            elif choice == "3":
                self.view_incidents()
            elif choice == "4":
                self.view_resources()
            elif choice == "5":
                self.allocate_resources()
            elif choice == "6":
                self.view_utilization_metrics()
            elif choice == "7":
                self.view_historical_data()
            elif choice == "8":
                print("Thank you for using the Emergency Resource Allocation System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def setup_users(self):
        """
        Initialize default users.
        """
        self.users.append(User(username="admin", password="admin123", role="admin"))
        self.users.append(User(username="coordinator", password="coord123", role="coordinator"))
        self.users.append(User(username="viewer", password="viewer123", role="viewer"))

    def authenticate_user(self):
        """
        Authenticate the user by prompting for a username and password.
        """
        print("\nUser Authentication")
        while True:
            username = input("Username: ")
            password = input("Password: ")
            for user in self.users:
                if user.authenticate(username, password):
                    self.current_user = user
                    print(f"Authentication successful! Welcome, {user.username}.")
                    self.logger.log(f"User logged in: {user.username} ({user.role})")
                    return
            print("Invalid username or password. Please try again.")

    def log_incident(self):
        print("\nEnter incident details:")
        location = input("Location: ")
        emergency_type = input("Type of emergency: ")
        priority = input("Priority level (high/medium/low): ")
        required_resources = input("Required resources (comma-separated): ").split(",")
        incident = {
            "location": location,
            "type": emergency_type,
            "priority": priority,
            "required_resources": [r.strip() for r in required_resources],
        }
        self.incidents.append(incident)
        print("Incident logged successfully!")
        self.logger.log(f"New incident logged: {incident}")
        self.save_historical_data()  # Save data after logging an incident

    def add_resource(self):
        print("\nEnter resource details:")
        resource_type = input("Resource type: ")
        location = input("Location: ")
        availability = input("Availability (yes/no): ").lower() == "yes"
        resource = {
            "type": resource_type,
            "location": location,
            "availability": availability,
        }
        self.resources.append(resource)
        print("Resource added successfully!")
        self.logger.log(f"New resource added: {resource}")
        self.save_historical_data()  # Save data after adding a resource

    def view_incidents(self):
        print("\nCurrent Incidents:")
        if not self.incidents:
            print("No incidents logged.")
        else:
            for i, incident in enumerate(self.incidents, 1):
                print(f"{i}. Location: {incident['location']}, Type: {incident['type']}, "
                      f"Priority: {incident['priority']}, Required Resources: {', '.join(incident['required_resources'])}")

    def view_resources(self):
        print("\nAvailable Resources:")
        if not self.resources:
            print("No resources available.")
        else:
            for i, resource in enumerate(self.resources, 1):
                print(f"{i}. Type: {resource['type']}, Location: {resource['location']}, "
                      f"Availability: {'Yes' if resource['availability'] else 'No'}")

    def allocate_resources(self):
        print("\nAllocating resources to incidents...")
        # Placeholder for allocation logic
        print("Resource allocation completed successfully!")

    def view_utilization_metrics(self):
        print("\nResource Utilization Metrics:")
        print(self.metrics_service.calculate_utilization())

    def view_historical_data(self):
        print("\nHistorical Data:")
        data = self.data_storage.load_data()
        self.incidents = data.get("incidents", [])
        self.resources = data.get("resources", [])
        print(data)

    def save_historical_data(self):
        """
        Save incidents and resources to the data storage.
        """
        self.data_storage.save_data({"incidents": self.incidents, "resources": self.resources})

    def load_historical_data(self):
        """
        Load incidents and resources from the data storage.
        """
        data = self.data_storage.load_data()
        self.incidents = data.get("incidents", [])
        self.resources = data.get("resources", [])



from datetime import datetime

from limsx.lims.base import LIMSBase
from limsx.lims.client import Client

class Sample(LIMSBase):
    VALID_STATUSES = ['pending', 'received', 'submitted', 'verified']

    def __init__(self, sample_type: str, client_instance: Client, test_order: str, collection_date: datetime, collection_point: str, status: str = 'pending', results=None):
        """Initialize a Sample instance with attributes."""
        super().__init__()
        self.sample_type = sample_type
        self.client = client_instance  # Use the renamed parameter
        self.test_order = test_order
        if not isinstance(collection_date, datetime):
            raise ValueError("collection_date must be a datetime object.")
        self.collection_date = collection_date
        self.collection_point = collection_point
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Must be one of {self.VALID_STATUSES}.")
        self.status = status
        self.results = results if results is not None else {}

    def update_status(self, new_status: str):
        """Update the status of the sample."""
        if new_status in self.VALID_STATUSES:
            self.status = new_status
            self.date_updated = datetime.now()
        else:
            raise ValueError(f"Invalid status '{new_status}'. Must be one of {self.VALID_STATUSES}.")

    def receive(self):
        """Change the sample status to 'received'."""
        self.update_status('received')

    def record_results(self, **kwargs):
        """Record test results with test parameters and their values."""
        self.results.update(kwargs)
        self.date_updated = datetime.now()

    def submit(self):
        """Change the sample status to 'submitted'."""
        if self.status != 'received':
            raise ValueError("Sample must be in 'received' status before submission.")
        self.update_status('submitted')

    def verify(self):
        """Change the sample status to 'verified'."""
        if self.status != 'submitted':
            raise ValueError("Sample must be in 'submitted' status before verification.")
        self.update_status('verified')

    def __repr__(self):
        return (f"<Sample("
                f"sample_type='{self.sample_type}', "
                f"client={self.client}, "
                f"test_order='{self.test_order}', "
                f"collection_date='{self.collection_date}', "
                f"collection_point='{self.collection_point}', "
                f"status='{self.status}', "
                f"results={self.results})>")

# Example usage
if __name__ == "__main__":
    client = Client("Omar", "Amour", "Male", datetime(1997, 5, 23).date())
    client1 = Client("Hamisa", "Omar", "Mahawi", datetime(1971, 3, 23).date())
    sample = Sample(
        sample_type="Blood",
        client_instance=client,
        test_order="CBC",
        collection_date=datetime.now(),
        collection_point="Main Lab",
        status="pending"
    )

    print(sample)  # This will now display the sample data correctly
    sample.receive()
    print(sample)
    sample.record_results(Hemoglobin="13.5 g/dL", WBC="6.2 x10^9/L")
    print(sample.results)  # This will display the results correctly
    sample.submit()
    print(sample)
    sample.verify()
    print(sample)

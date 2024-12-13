# records.py
from datetime import datetime
from limsx.lims.client import Client
from limsx.lims.base import LIMSBase
from limsx.lims.sample import Sample  # Assuming Sample is defined in this module
class MedicalRecord(LIMSBase):
    def __init__(self, client, sample, results):
        """
        Initialize a MedicalRecord instance.

        Parameters:
        client (Client): The client associated with the medical record.
        sample (Sample): The sample associated with the medical record.
        results (dict): A dictionary containing the medical results.
        """
        super().__init__()
        self.client = client
        self.sample = sample
        self.results = results

    def __repr__(self):
        return (f"<MedicalRecord("
                f"client={self.client}, "
                f"sample={self.sample}, "
                f"results={self.results})>")

    def update_results(self, **kwargs):
        """Update the medical results with new values."""
        self.results.update(kwargs)

# Example usage


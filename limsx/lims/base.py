""""Sample base"""
import uuid
from datetime import datetime

class LIMSBase:
    def __init__(self):
        """Initialize the base LIMS class with automatic UUID and datetime attributes."""
        self.id = str(uuid.uuid4())
        self.date_created = datetime.now()
        self.date_updated = datetime.now()

    def to_dict(self):
        """Convert the instance's attributes into a dictionary representation."""
        return self.__dict__

    def __repr__(self):
        """Provide a formal string representation of the instance."""
        class_name = self.__class__.__name__
        attributes = {key: value for key, value in self.__dict__.items()}
        return f"<{class_name}: ({attributes})>"

# Example usage
if __name__ == "__main__":
    instance = LIMSBase()
    print(instance)  # Formal string representation
    print(instance.to_dict())  # Dictionary representation




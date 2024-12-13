from datetime import date

from limsx.lims.base import LIMSBase

from datetime import date
from limsx.lims.base import LIMSBase  # Replace with the absolute import path


class Client(LIMSBase):
    def __init__(self, first_name: str, last_name: str, gender: str, birth_date: date, medical_records=None):
        """Initialize a Client instance with personal details and medical records."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date
        self.medical_records = medical_records \
            if medical_records is not None\
            else []

    def __repr__(self):
        """Provide a formal string representation of the Client instance."""
        #class_name = self.__class__.__name__
        #attributes = {key: value for key, value in self.__dict__.items()}
        #return f"<{class_name}: ({attributes})>"
        return f"{self.__class__.__name__} : ({self.__dict__})"




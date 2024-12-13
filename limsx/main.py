from datetime import datetime,date
from limsx.lims.client import Client # Adjust the path to match your project structure
from limsx.lims.sample import Sample
from limsx.lims.records import MedicalRecord
from limsx.lims.user import User

if __name__ == "__main__":
    client = Client("Omar", "Salum", "Amour", date(1997, 5, 23))
    client1 = Client("Hamisa", "Omar", "Mahawi", date(1971, 3, 23))

    sample = Sample(
        sample_type="Blood",
        client_instance=client,
        test_order="CBC",
        collection_date=datetime.now(),
        collection_point="Main Lab",
        status="pending"
    )

    user = User(full_name="Robert senior", username="robtheIII", password="secure password")
    print(client)  # Formal string representation
    #print(client.to_dict())  # Dictionary representation
    print("\n")
    print(client1)



    print(sample)  # This will now display the sample data correctly
    sample.receive()
    print(sample)
    sample.record_results(Hemoglobin="13.5 g/dL", WBC="6.2 x10^9/L")
    print(sample.results)  # This will display the results correctly
    sample.submit()
    print(sample)
    sample.verify()
    print(sample)


    # Create a medical record
    results = {
        "Hemoglobin": "13.5 g/dL",
        "WBC": "6.2 x10^9/L"
    }
    medical_record = MedicalRecord(client, sample, results)

    # Print the medical record
    print(medical_record)

    # Update results
    medical_record.update_results(Platelets="250 x10^9/L")
    print(medical_record)



    print("\n")
    # Print the user details before login
    print(user)

    # Log in the user
    user.login()

    # Print the user details after login
    print(user)

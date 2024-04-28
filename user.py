import requests

# Base URL for the FastAPI server
BASE_URL = "http://127.0.0.1:8000"


# Function to create an item
def create_item(name, price, quantity):
    data = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    response = requests.post(f"{BASE_URL}/items/", json=data)
    print(response.json())

# Function to get all items
def read_all():
    response = requests.get(f"{BASE_URL}/items")
    print(response.json())

# Function to get an item by ID
def read_item(name):
    response = requests.get(f"{BASE_URL}/items/{name}")
    print(response.json())


# Function to update an item by ID
def update_item(name, price, quantity):
    data = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    response = requests.put(f"{BASE_URL}/items/{name}", json=data)
    print(response.json())


# Function to delete an item by ID
def delete_item(name):
    response = requests.delete(f"{BASE_URL}/items/{name}")
    print(response.json())


# Example usage
if __name__ == "__main__":
    # Create an item
    create_item("TCS", 50.10, 5)

    #Check all
    read_all()

    # Get an item
    read_item("INFOSYS")

    # Update an item
    update_item("INFOSYS", 40.70, 11)

    # Check all
    read_all()

    # Delete an item
    delete_item("TCS")
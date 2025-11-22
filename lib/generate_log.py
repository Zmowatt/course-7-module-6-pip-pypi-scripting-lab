from datetime import datetime
import os
import requests

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename


    # STEP 1:
    if not isinstance(data, list):
        raise TypeError("Input data must be a list.")

    # STEP 2:
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3:
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4:
    print(f"Log successfully written to {filename}")
    
    return filename

def fetch_data():

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=10
        )
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

    if response.status_code == 200:
        return response.json()

    print(f"Request failed with status code: {response.status_code}")
    return{}

if __name__ == "__main__":
    sample_logs = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_logs)
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
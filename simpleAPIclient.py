import requests
API_URL = "https://jsonplaceholder.typicode.com/users"
def get_users():
    try:
        print("Connecting to API...")
        print()
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            users = response.json()
            print("**************************************")
            print("         USER INFORMATION")
            print("**************************************")
            for user in users:
                print("ID      :", user["id"])
                print("Name    :", user["name"])
                print("Email   :", user["email"])
                print("Username:", user["username"])
                print("City    :", user["address"]["city"])
                print("--------------------------------------")
        else:
            print("API request failed.")
            print("Status Code:", response.status_code)
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API.")
        print("Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: API request timed out.")
    except requests.exceptions.RequestException as error:
        print("Error while making API request:", error)
get_users()



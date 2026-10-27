### **Simple API Client Using Python**



###### **Project Overview**



This project demonstrates how to build a simple API client using Python.



The program connects to a public REST API, retrieves user information in JSON format, processes the response, and displays selected information such as user ID, name, email, username, and city.



The project also includes error-handling logic for connection failures, timeout errors, and other request-related errors.



###### **Objective**



The main objective of this project is to understand:



\- How APIs work

\- How to send a GET request using Python

\- How to use the `requests` library

\- How to receive JSON data from an API

\- How to convert JSON data into Python data

\- How to extract required information from JSON

\- How to check HTTP status codes

\- How to handle API errors



###### **Technologies Used**

\- Python

\- Requests Library

\- REST API

\- JSON

\- JSONPlaceholder Public API



###### 

###### **API Used**



The project uses the JSONPlaceholder public API.

API Endpoint:

https://jsonplaceholder.typicode.com/users

This API provides sample user information.



###### **Requirements**



Before running the project, make sure Python is installed.



Check Python version:

python --version



Install the `requests` library:

pip install requests



###### **Complete Program**

import requests



API\_URL = "https://jsonplaceholder.typicode.com/users"





def get\_users():

&#x20;   try:

&#x20;       print("Connecting to API...")

&#x20;       print()



&#x20;       response = requests.get(API\_URL, timeout=10)



&#x20;       if response.status\_code == 200:



&#x20;           users = response.json()



&#x20;           print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

&#x20;           print("         USER INFORMATION")

&#x20;           print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")



&#x20;           for user in users:



&#x20;               print("ID      :", user\["id"])

&#x20;               print("Name    :", user\["name"])

&#x20;               print("Email   :", user\["email"])

&#x20;               print("Username:", user\["username"])

&#x20;               print("City    :", user\["address"]\["city"])



&#x20;               print("--------------------------------------")



&#x20;       else:



&#x20;           print("API request failed.")

&#x20;           print("Status Code:", response.status\_code)



&#x20;   except requests.exceptions.ConnectionError:



&#x20;       print("Error: Unable to connect to the API.")

&#x20;       print("Please check your internet connection.")



&#x20;   except requests.exceptions.Timeout:



&#x20;       print("Error: API request timed out.")



&#x20;   except requests.exceptions.RequestException as error:



&#x20;       print("Error while making API request:", error)





get\_users()



###### **Important Code Explanation**



**1. Import Requests**

import requests

The `requests` library is used to send HTTP requests from Python.



**2. Store API URL**

API\_URL = "https://jsonplaceholder.typicode.com/users"

This stores the address of the public API.



**3. Send GET Request**

response = requests.get(API\_URL, timeout=10)

The `GET` request asks the API to provide user information.

The `timeout=10` means the program will wait for a maximum of 10 seconds for the response.



**4. Check Status Code**

if response.status\_code == 200:

HTTP status code `200` means that the request was successful.



**5. Convert JSON Response**

users = response.json()

This converts the JSON response received from the API into Python data.



**6. Loop Through Users**

for user in users:

The loop processes each user one by one.



**7. Display Selected Information**



print("ID      :", user\["id"])

print("Name    :", user\["name"])

print("Email   :", user\["email"])

print("Username:", user\["username"])

print("City    :", user\["address"]\["city"])



The program extracts and displays selected information from each user.

###### 

###### **Sample Output**



Connecting to API...



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;        USER INFORMATION

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ID      : 1

Name    : Leanne Graham

Email   : Sincere@april.biz

Username: Bret

City    : Gwenborough

\--------------------------------------

ID      : 2

Name    : Ervin Howell

Email   : Shanna@melissa.tv

Username: Antonette

City    : Wisokyburgh

\--------------------------------------

ID      : 3

Name    : Clementine Bauch

Email   : Nathan@yesenia.net

Username: Samantha

City    : McKenziehaven

\--------------------------------------

ID      : 4

Name    : Patricia Lebsack

Email   : Julianne.OConner@kory.org

Username: Karianne

City    : South Elvis

\--------------------------------------

ID      : 5

Name    : Chelsey Dietrich

Email   : Lucio\_Hettinger@annie.ca

Username: Kamren

City    : Roscoeview

\--------------------------------------

ID      : 6

Name    : Mrs. Dennis Schulist

Email   : Karley\_Dach@jasper.info

Username: Leopoldo\_Corkery

City    : South Christy

\--------------------------------------

ID      : 7

Name    : Kurtis Weissnat

Email   : Telly.Hoeger@billy.biz

Username: Elwyn.Skiles

City    : Howemouth

\--------------------------------------

ID      : 8

Name    : Nicholas Runolfsdottir V

Email   : Sherwood@rosamund.me

Username: Maxime\_Nienow

City    : Aliyaview

\--------------------------------------

ID      : 9

Name    : Glenna Reichert

Email   : Chaim\_McDermott@dana.io

Username: Delphine

City    : Bartholomebury

\--------------------------------------

ID      : 10

Name    : Clementina DuBuque

Email   : Rey.Padberg@karina.biz

Username: Moriah.Stanton

City    : Lebsackbury

\--------------------------------------



###### **Error Handling**



The project handles different API-related errors.

Connection Error

except requests.exceptions.ConnectionError:

This handles situations where the program cannot connect to the API.

Timeout Error

except requests.exceptions.Timeout:

This handles situations where the API takes too long to respond.

Request Error

except requests.exceptions.RequestException as error:

This handles other request-related errors.

HTTP Status Code

The project checks whether the API request was successful.

200 → Successful request

If the status code is not 200, the program displays the status code.



###### **Key Concepts Learned**

REST API

HTTP

GET request

HTTP status codes

JSON

Python dictionaries and lists

requests library

Exception handling

JSON response processing



###### **Conclusion**



The Simple API Client project demonstrates how Python can communicate with a public REST API.



The program successfully sends a GET request, receives JSON data, converts the response into Python data, extracts useful information, and displays it in a clean format.



The project also demonstrates basic error handling, making the program more reliable when network or API problems occur.


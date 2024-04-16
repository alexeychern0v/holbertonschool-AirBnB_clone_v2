#!/usr/bin/python3
"""Gets and displays todo list of an employee"""
import requests
from sys import argv


def callapi(id):
    """Calls the api, parses data and prints result"""
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    req = requests.get(url, params={"_expand": "user"})
    data = req.json()
    
    TASK_TITLE = [task["title"] for task in data if task["completed"]]
    EMPLOYEE_NAME = data[0]["user"]["name"]
    NUMBER_OF_DONE_TASKS = len(TASK_TITLE)
    TOTAL_NUMBER_OF_TASKS = len(data)
    
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    
    for task_title in TASK_TITLE:
        print("\t {}".format(task_title))


if __name__ == "__main__":
    """Main function"""
    if len(argv) != 2:
        print("Usage: python3 {} (int)id_employe".format(__file__))
        exit(1)
    callapi(argv[1])
    
#!/usr/bin/python3
"""
Python script to export data from a REST API to a CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        
        # Fetch user information
        user_req = requests.get("{}users/{}".format(url, user_id))
        username = user_req.json().get("username")
        
        # Fetch user todo tasks
        todo_req = requests.get("{}todos?userId={}".format(url, user_id))
        tasks = todo_req.json()
        
        # Write directly to the CSV file named after the USER_ID
        filename = "{}.csv".format(user_id)
        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow([
                    user_id,
                    username,
                    task.get("completed"),
                    task.get("title")
                ])

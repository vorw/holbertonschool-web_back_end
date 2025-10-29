#!/usr/bin/env python3
"""provide stats about Nginx logs stored in db"""


from pymongo import MongoClient


def main():
    """Print required stats"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    total = collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
        status_count = collection.count_documents({"method": "GET", "path": "/status"})
        print(f"{status_count} status check")
    if __name__ == "__main__":
        main()

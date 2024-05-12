#!/usr/bin/env python3

"""
log doc
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_ng = client.logs.nginx

    count = logs_ng.estimated_document_count()

    print(f'{count} logs')
    print('Methods:')

    for mt in ("GET", "POST", "PUT", "PATCH", "DELETE"):
        print('\tMethod {}: {}'.format(mt,
              logs_ng.count_documents({'method': mt})))

    print('{} status check'.format(
          logs_ng.count_documents({'method': 'GET', 'path': '/status'})))

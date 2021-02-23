import re
from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')


def match():
    result = client['comic-book']['DC'].aggregate([
        {
            '$match': {
                'name': re.compile(r"Batman")
            }
        }
    ])

    pprint.pprint(list(result))

from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')


def run(collection, pipeline):
    result = client['comic-book'][collection].aggregate(
        pipeline, allowDiskUse=True
    )

    pprint.pprint(list(result))

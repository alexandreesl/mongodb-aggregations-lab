from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')


def run(pipeline):
    result = client['comic-book']['DC'].aggregate(
        pipeline
    )

    pprint.pprint(list(result))

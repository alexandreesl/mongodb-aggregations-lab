import re

from aggregations.aggregations import run


def main():
    run([{
        '$match': {
            'name': re.compile(r"Flash ", flags=re.IGNORECASE),
            'ALIGN': 'Good Characters'
        }
    },
        {
            '$project': {
                'FIRST APPEARANCE': 1, 'name': 1, '_id': 0
            }
        }])
    print('------------------------------------------------------')
    run([
        {
            '$match': {
                'FIRST APPEARANCE': {'$exists': True}
            }
        },
        {
            '$project': {
                '_id': 0,
                'name': 1,
                'year': {'$toInt': {'$arrayElemAt': [{'$split': [{'$toString': '$FIRST APPEARANCE'}, ","]}, 0]}}
            }
        },
        {
            '$match': {
                'year': {"$gte": 1956, "$lte": 1970}
            }
        }
    ])


if __name__ == "__main__":
    main()

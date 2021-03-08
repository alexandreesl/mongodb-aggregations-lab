import re

from aggregations.aggregations import run


def main():
    run('DC', [{
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
    run('DC', [
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
    print('------------------------------------------------------')
    run('DC', [
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
        },
        {
            '$sort': {
                'name': 1
            }
        }
    ])
    print('------------------------------------------------------')
    run('DC', [
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
        },
        {
            '$count': 'total'
        }
    ])
    print('------------------------------------------------------')
    run('Marvel', [
        {
            '$match': {
                'ALIGN': {'$exists': True}
            }
        },
        {
            '$group': {
                '_id': '$ALIGN',
                'count': {'$sum': 1}
            }
        }
    ])
    print('------------------------------------------------------')
    run('Marvel', [
        {
            '$match': {
                'ALIGN': {'$exists': True}
            }
        },
        {
            '$group': {
                '_id': '$ALIGN',
                'count': {'$sum': 1}
            }
        }
    ])
    print('------------------------------------------------------')
    run('Marvel', [
        {
            '$bucket': {
                'groupBy': "$Year",
                'boundaries': [1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020],
                'default': "Unknown",
                'output': {
                    'count': {'$sum': 1}
                }
            }
        }
    ])
    print('------------------------------------------------------')
    run('DC', [
        {
            '$match': {
                'YEAR': {'$exists': True}
            }
        },
        {
            '$bucketAuto': {
                'groupBy': '$YEAR',
                'buckets': 10,
                'granularity': 'E192',
                'output': {
                    'count': {'$sum': 1}
                }
            }
        }
    ])
    print('------------------------------------------------------')
    run('DC', [
        {
            '$facet': {
                'Silver age characters': [
                    {
                        '$match': {
                            'FIRST APPEARANCE': {'$exists': True}
                        }
                    },
                    {
                        '$project': {
                            '_id': 0,
                            'name': 1,
                            'year': {
                                '$toInt': {'$arrayElemAt': [{'$split': [{'$toString': '$FIRST APPEARANCE'}, ","]}, 0]}}
                        }
                    },
                    {
                        '$match': {
                            'year': {"$gte": 1956, "$lte": 1970}
                        }
                    },
                    {
                        '$sort': {
                            'name': 1
                        }
                    }
                ],
                'Characters by decade': [
                    {
                        '$bucket': {
                            'groupBy': "$YEAR",
                            'boundaries': [1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020],
                            'default': "Unknown",
                            'output': {
                                'count': {'$sum': 1}
                            }
                        }
                    }
                ]
            }
        },
        {'$out': 'DC-reports'}
    ])


if __name__ == "__main__":
    main()

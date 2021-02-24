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



if __name__ == "__main__":
    main()

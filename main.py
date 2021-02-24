import re

from aggregations.aggregations import run


def main():
    run({
        '$match': {
            'name': re.compile(r"Flash")
        }
    })


if __name__ == "__main__":
    main()

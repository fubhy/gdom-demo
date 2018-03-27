import json
import sys
from gdom import schema

def main():
    with open('query.gql', 'r') as gql:
        query=gql.read().replace('\n', '')

    execution = schema.execute(query)
    if execution.errors:
        raise Exception(execution.errors[0])

    print json.dumps(execution.data, indent=4)

if __name__ == '__main__':
    main()

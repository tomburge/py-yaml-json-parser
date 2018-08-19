# Author: Tom Burge
# Title: py-yaml-json-parser
# Description: Simple Menu-Based YAML/JSON Parser
# Requirements:
#   - Ruamel.YAML (pip install ruamel.yaml

import json
import sys
from collections.abc import Mapping, Sequence
from collections import OrderedDict
import ruamel.yaml
from ruamel.yaml.error import YAMLError
from ruamel.yaml.comments import CommentedMap

yaml = ruamel.yaml.YAML()


def printmenu():
    menu = ('1. Parse YAML to JSON\n'
            '2. Parse JSON to YAML\n'
            '3. Exit\n'
            )
    print(menu)


class OrderlyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Mapping):
            return OrderedDict(o)
        elif isinstance(o, Sequence):
            return list(o)
        return json.JSONEncoder.default(self, o)


def parseyaml(intype, outtype):
    infile = input('Please enter a {} filename to parse: '.format(intype))
    outfile = input('Please enter a {} filename to output: '.format(outtype))

    with open(infile, 'r') as stream:
        try:
            datamap = yaml.load(stream)
            with open(outfile, 'w') as output:
                output.write(OrderlyJSONEncoder(indent=2).encode(datamap))
        except YAMLError as exc:
            print(exc)
            return False
    print('Your file has been parsed.\n\n')


def parsejson(intype, outtype):
    infile = input('Please enter a {} filename to parse: '.format(intype))
    outfile = input('Please enter a {} filename to output: '.format(outtype))

    with open(infile, 'r') as stream:
        try:
            datamap = json.load(stream, object_pairs_hook=CommentedMap)
            with open(outfile, 'w') as output:
                yaml.dump(datamap, output)
        except YAMLError as exc:
            print(exc)
            return False

    print('Your file has been parsed.\n\n')


loop = True

while loop:
    printmenu()  # Prints Menu for User
    choice = int(input('Please select an operation: '))

    if choice == 1:
        infiletype = 'YAML'
        outfiletype = 'JSON'
        parseyaml(infiletype, outfiletype)
    elif choice == 2:
        infiletype = 'JSON'
        outfiletype = 'YAML'
        parsejson(infiletype, outfiletype)
    elif choice == 3:
        sys.exit(0)
    else:
        print('Please make a selection')

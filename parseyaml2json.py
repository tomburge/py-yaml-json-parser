# Author: Tom Burge
# Title: py-yaml-json-parser
# Description: Simple Menu-Based YAML/JSON Parser
# Requirements:
#   - PyYAML (pip install pyyaml)

import json
import yaml
import sys


def printmenu():
    menu = ('1. Parse YAML to JSON\n'
            '2. Parse JSON to YAML\n'
            '3. Exit\n'
            )
    print(menu)


def parseyaml(intype, outtype):
    infile = input('Please enter a {} filename to parse: '.format(intype))
    outfile = input('Please enter a {} filename to output: '.format(outtype))

    with open(infile, 'r') as stream:
        try:
            datamap = yaml.safe_load(stream)
            with open(outfile, 'w') as output:
                json.dump(datamap, output)
        except yaml.YAMLError as exc:
            print(exc)

    print('Your file has been parsed.\n\n')


def parsejson(intype, outtype):
    infile = input('Please enter a {} filename to parse: '.format(intype))
    outfile = input('Please enter a {} filename to output: '.format(outtype))

    with open(infile, 'r') as stream:
        try:
            datamap = json.load(stream)
            with open(outfile, 'w') as output:
                yaml.dump(datamap, output)
        except yaml.YAMLError as exc:
            print(exc)

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

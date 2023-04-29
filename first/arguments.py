# how to pass arguments in the python
# import sys
import argparse
# print(sys.argv)

parser = argparse.ArgumentParser(description='This print the')

parser.add_argument('-c', '--color', metavar='color', required=True, choices={"abhay","pandey"}, help="The color to search")

args = parser.parse_args()

print("Hekllo ")
print(args.color)
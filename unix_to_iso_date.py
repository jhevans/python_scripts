import datetime
import time
import argparse
import sys

parser = argparse.ArgumentParser(description="Date conversion tool")
parser.add_argument("input_string", metavar="S", type=str, help="The string to be converted")
parser.add_argument("--reverse", nargs='?', default=False, help="Reverse the operation converting an isoformat date to a unix timestamp")

# value = sys.argv[1]
args = parser.parse_args()
if args.reverse:
    value = args.input_string
    d = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%Z")
    print (time.mktime(d.timetuple()))
else:
    value = int(float(args.input_string))
    
    try:
        d = datetime.datetime.fromtimestamp(value)
        print (time.mktime(d.timetuple()))
    except ValueError:
        # May be in milliseconds if so correct
        value /= 1000
        d = datetime.datetime.fromtimestamp(value)
    
    print(d.isoformat())

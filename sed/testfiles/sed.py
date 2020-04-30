import sys
import re

script = sys.argv[1]
files = sys.argv[2:]

def parse_script(script):
    if script[0] == "s":
        return ('s', script.split('/')[1:3])
    else:
        print("Error, only s supported")
        sys.exit(1)

def do_s(file_name, pattern, replace):
    pattern, replace = args
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            fixed = re.sub(pattern, replace, line)
            print(fixed, end="")

def apply_script(command, file_name, args):
    if command == "s":
        do_s(file_name, *args)
    else:
        print("Not supported")
        sys.exit(1)


command, args =  parse_script(script)
for file_name in files:
   apply_script(command, file_name, args)

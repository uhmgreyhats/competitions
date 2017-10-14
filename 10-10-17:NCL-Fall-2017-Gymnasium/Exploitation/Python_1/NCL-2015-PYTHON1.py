#!/usr/bin/python

import sys

def main():
  if len(sys.argv) != 2:
    print "Invalid args"
    return
  password = sys.argv[1]
  builder = 0
  for c in password:
    builder += ord(c)
  if builder == 1000 and len(password) == 10 and ord(password[1]) == 83:
    print "correct"
  else:
    print "incorrect"

if __name__ == "__main__":
  main()


#!/usr/bin/python
#this is string op file

str1="Hello world, we all over the world!"

print "the orignal string is: \r\n\t{0}".format(str1)

print "to lower: {0}".format(str1.lower())
print "to upper: {0}".format(str1.upper())
print "Swapcase: {0}".format(str1.swapcase())
print "Captalize:  {0}".format(str1.capitalize())
print "split of ' ' is:{0}".format(str1.split())
print "split of ',' is:{0}".format(str1.split(','))

print "is find 'al'? index is: {0}".format(str1.find('al'))
print "is find 'AB'? index is: {0}".format(str1.find('AB'))

import traceback

try:
    print "is index 'al'? index is: {0}".format(str1.index('al'))
    print "is index 'AB'? index is: {0}".format(str1.index('AB'))
except Exception,ex:
    print Exception,":",ex

print "replace 'o' to 'X' is: {0}".format(str1.replace('o', 'X'))

print "lstrip 'He!dl' is: {0}".format(str1.lstrip('He!dl'))
print "rstrip 'He!dl' is: {0}".format(str1.rstrip('He!dl'))
print "strip  'He!dl' is: {0}".format(str1.strip('He!dl'))


#!/bin/python3

import math
import os
import random
import re
import sys
from codecs import ignore_errors

#
# Complete the 'formatPhoneNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING country_name
#  2. STRING phone_number
#

import requests


# import json

def formatPhoneNumber(country_name, phone_number):
    pass
    # Write your code here


def getPhoneNumber(country_name, phone_number):
    parameters = {"name": country_name, "page": 1}
    # headers = {"content-type": "application/json"}
    response = requests.get('https://jsonmock.hackerrank.com/api/countries', params=parameters)
    res = response.json()
    return res


    # API is not responding.



country_name = input("Enter country Name: ")
phone_number = input("Enter Phone NUmber: ")
result = getPhoneNumber(country_name, phone_number)
print(f"Result is: {result}")

data = result["data"]
print(f"Data is: {data}")




# if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # country_name = input()
    #
    # phone_number = input()
    #
    # result = getPhoneNumber(country_name, phone_number)

    # fptr.write(result + '\n')

    # fptr.close()




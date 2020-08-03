#!/usr/bin/python
import requests
import pytest
import sys
import json
import pytest

def main(args):
  testCountry(args[1], args[2]) #Positive TestCase
  testCountry2(args[1], "testbadData") #Negative TestCase. 

def getCapital(country):
  url = "https://restcountries.eu/rest/v2/name/{country}".format(country=country)
  response = requests.get(url)
  json_data = response.json()
  try:
    if (len(json_data)) >= 2:
      return json_data[1][u'capital']
    else:
      return json_data[0][u'capital']
  except:
      return "Country not found"

def testCountry(countryName, expectedName):
  assert getCapital(countryName) == expectedName
  print "Test case testCountry passed"

def testCountry2(countryName, badData):
  assert getCapital(countryName) != badData
  print "Test case testCountry2 passed"
    
if __name__  == "__main__":
 while True:
   if (len(sys.argv)) > 3:
     print "You have exceeded the maximum number of parameters" 
     sys.exit()
   main(sys.argv)
   input = raw_input()
   if input == "exit":
      print "The program will now exit"
      sys.exit()

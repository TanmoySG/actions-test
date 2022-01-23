import json

with open("config.json", "r") as testFile:
  jsObj = json.load(testFile)
  
major, minor, bug = jsObj["version"].split(".")

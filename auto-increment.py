import json

with open("config.json", "r") as testFile:
    jsObj = json.load(testFile)

major, minor, bug = jsObj["version"].split(".")

major = int(major)+1

jsObj["version"] = str(major)+"."+str(minor)+"."+str(bug)

with open("config.json", "w") as testFile:
	json.dump(jsObj, testFile, indent=4)
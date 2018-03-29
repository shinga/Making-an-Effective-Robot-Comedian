import urllib, json

url = "http://127.0.0.1:5000/showHeuristics"

response = urllib.urlopen(url)
data = json.loads(response.read())
print data

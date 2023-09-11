import requests

print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/philiponions/CMPUT404-Lab1/main/script.py")
print(r.text)

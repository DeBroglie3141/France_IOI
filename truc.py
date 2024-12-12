import requests
import webbrowser

response = requests.get(    
    "https://http-first-steps.challenges.pro.root-me.org/",
    headers={
        "pizza" : "pizza",
        "b" : "rien",
        "c" : "rien",
        "v" : "rien",
        "d" : "rien",
        "z" : "rien",
        "r" : "rien",
        "oiu" : "oij",
        "oaziu" : "oij",
        "pineapple" : "pineapple",
        }
)

with open("truc.html", "wb") as f:
    f.write(response.content)

webbrowser.open("truc.html")
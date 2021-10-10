import requests
import json

def getRepos(username):
    nameResponse = requests.get("https://api.github.com/users/"+username+"/repos")
    i = 0
    while i < len(nameResponse.json()):
        name = nameResponse.json()[i]['name']
        commitsResponse = requests.get("https://api.github.com/repos/"+username+"/"+name+"/commits")
        commits = str(len(commitsResponse.json()))
        print("Repo: " + name + " Number of commits: " + commits)
        i += 1

def main():
    username = input("Enter your GitHub username:");
    getRepos(username)

main()

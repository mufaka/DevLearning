import json 
import requests 
import sys 

def main():
    if len(sys.argv) != 2:
        sys.exit("Band name not provided")
    
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=20&term={sys.argv[1]}")

    o = response.json()
    for result in o["results"]:
        print(result["trackName"])

if __name__ == "__main__":
    main()
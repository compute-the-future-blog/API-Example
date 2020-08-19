import requests
import json
import time


def main():
    url = "https://official-joke-api.appspot.com/jokes/random"
    while True:
        response = requests.get(url)

        response_dict = json.loads(response.text)
        setup = response_dict["setup"]
        punchline = response_dict["punchline"]


        print(setup)
        for i in range(3):
            time.sleep(1)
            print("...")
        print(punchline)
        input()



if __name__ == "__main__":
    main()

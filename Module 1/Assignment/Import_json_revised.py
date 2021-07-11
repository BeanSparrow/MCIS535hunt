import json

def json_parser(): 
    with open('data/data-text.json') as f:
        data = json.load(f)

    for item in data:
        print(item)

def main():
    json_parser()


if __name__ == "__main__":
    main()



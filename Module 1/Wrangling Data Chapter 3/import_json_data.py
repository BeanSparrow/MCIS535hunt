import json

def json_reader():
    json_data = open('data/data-text.json').read()

    data = json.loads(json_data)

    for item in data:
        print(item)

def main():
    json_reader()

if __name__ == "__main__":
    main()
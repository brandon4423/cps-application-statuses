import json
import time


def test():
    start_time = time.time()

    with open('cps.json', 'r') as file:
        data1 = json.load(file)

    with open('gspread.json', 'r') as file:
        data2 = json.load(file)

    address = data1['Address']
    id = data2
    print(address)
    print(id[1])

    end_time = time.time()
    final_time = end_time - start_time
    print(f"Run in: {final_time} seconds")

def main():
    test()

if __name__ == "__main__":
    main()
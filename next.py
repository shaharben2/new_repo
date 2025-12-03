import functools


def main():
    with open(input("enter path: "), "r") as file:
        print(functools.reduce(max, file.read().split("\n")))
        

if __name__ == '__main__':
    main()
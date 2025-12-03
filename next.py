import functools


def main():
    with open(input("enter path: "), "r") as file:
        print(functools.reduce(lambda x, y: x + y, map(len, file.read().split("\n"))))
        

if __name__ == '__main__':
    main()
import functools


def main():
    with open(input("enter path: "), "r") as file:
        search_len = int(input("Enter length: "))
        print("\n".join(list(filter(lambda name: len(name) == search_len, file.read().split("\n")))))
        

if __name__ == '__main__':
    main()
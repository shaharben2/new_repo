import functools


def main():
    with open(input("enter path: "), "r") as file:
        read_file = file.read().split("\n")
        min_len = len(min(read_file, key = len))
        print("\n".join(list(filter(lambda name: len(name) == min_len, read_file))))
        

if __name__ == '__main__':
    main()
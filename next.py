import functools


def main():
    with open(input("enter path: "), "r") as file1:
        with open(input("enter path: "), "w") as file2:
            file2.write("\n".join(map(str, map(len, file1.read().split("\n")))))
        

if __name__ == '__main__':
    main()
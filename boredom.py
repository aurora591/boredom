import os

def is_file(path_of_file):
    """
    this function gets a path and print is content if its a file, if not it will return exception
    :param path_of_file: string of path
    :return: print the content if a file, print error if not
    """
    try:
        with open(path_of_file, 'r') as f:
            content = f.read()
            print(content)
    except IOError:
        print("Error: file not found")


def boredom():
    """
    this function asks for paths of a folder and if its not exist it will print error and ask for another path,
     if it is exists it will go to function is file who print the content if it is a file
    :return:
    """
    while True:
        path = input("enter a path")
        try:
            files = os.listdir(path)
            for i in range(len(files)):
                first_file = files[i]
                path_of_file = os.path.join(path, first_file)
                is_file(path_of_file)
        except IOError:
            print("Error: path not found")

def main():
    boredom()
if __name__ == "__main__":
    main()
import os
import re
def main():
    read("test.html")

def parse(file, path="parse.txt"):
    m = re.findall('(?<=\>)(.*?)(?=\<)',file)
    with open(path, 'w') as file:
        file.write(str(m));
        file.close()
    
def read(path):
    with open(path, 'r') as file:
        parse(str(file.read()))
        file.close();

if __name__ == "__main__":
    main()

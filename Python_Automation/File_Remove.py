import os
def main():
    try:
        #fobj.remove() not applicable
        os.remove("fileDemo.txt")
        
    except FileNotFoundError as fobj:
        print("file is not found in directory")    


if __name__ == '__main__':
    main()
    
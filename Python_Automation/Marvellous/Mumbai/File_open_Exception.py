def main():
    try:
        open("FileDemo.txt","r")
        print("file gets opened")
        
    except FileNotFoundError as fobj:
        print("file is not found in directory")    


if __name__ == '__main__':
    main()
    
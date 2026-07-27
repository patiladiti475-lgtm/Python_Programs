def main():
    try:
        open("FileDemo.txt","w")
        print("file gets opened")
        
    except FileNotFoundError as fobj:
        print("file is not found in directory")    


if __name__ == '__main__':
    main()
    
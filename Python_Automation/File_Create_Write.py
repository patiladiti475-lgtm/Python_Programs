def main():
    try:
        fobj = open("FileDemo.txt","w")
        print("file gets opened")
        fobj.write("Jay ganesh......")
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("file is not found in directory")    


if __name__ == '__main__':
    main()
    
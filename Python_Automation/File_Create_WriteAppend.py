def main():
    try:
        fobj = open("FileDemo.txt","a")
        print("file gets opened")
        fobj.write("Pune Maharastra.....")
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("file is not found in directory")    


if __name__ == '__main__':
    main()
    
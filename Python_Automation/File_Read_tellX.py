def main():
    try:
        fobj = open("FileDemo.txt","r")
        print("file gets opened")
        print("File offset is : ", fobj.tell())
        Data = fobj.read(10)
        
        print(Data)
        
        print("File offset is : ", fobj.tell())
        
        Data = fobj.read(10)
        
        print(Data)
        
        print("File offset is : ", fobj.tell())
        
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("file is not found in directory")    


if __name__ == '__main__':
    main()
    
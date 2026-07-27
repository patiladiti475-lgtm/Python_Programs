#seek(kutha, kuthun)
#from where:0/1/2

#0 starting
#1 current
#2 end

def main():
    try:
        fobj = open("FileDemo.txt","r")
        print("file gets opened")
        
        fobj.seek(10,0)
        Data = fobj.read()
        print(Data)
        
    except FileNotFoundError as fobj:
        print("file is not found in directory")  
if __name__ == "__main__":
    main()        
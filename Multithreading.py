import threading

def Display(no):
    print(f"inside Display {no} :", threading.get_ident())
    
    
def main():
    print("inside Main:", threading.get_ident())
    
    tobj = threading.Thread(target=Display, args=(11,))
    
    tobj.start()   

if __name__ == "__main__":
    main()
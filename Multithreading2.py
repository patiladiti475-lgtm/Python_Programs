import threading

def Display():
    print("inside Display:", threading.get_ident())
    
    
def main():
    print("inside Main:", threading.get_ident())
    
    tobj = threading.Thread(target=Display)
    
    tobj.start()   

if __name__ == "__main__":
    main()
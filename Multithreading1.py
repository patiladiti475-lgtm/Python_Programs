import threading

def Display():
    print("inside Display:", threading.get_ident())
    
    
def main():
    print("inside Main:", threading.get_ident())
    Display()
    
    

if __name__ == "__main__":
    main()
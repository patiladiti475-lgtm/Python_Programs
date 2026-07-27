def main():
    marks = [90,78,56,98,77]
    
    for no in marks:
        print(no)
    print("_"*15)    
    marks[2] = 59 
    for no in marks:
        print(no)
    
if __name__ == "__main__":
    main()
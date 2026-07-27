# ---------------------------------------------------------
# Question:
# Write a program which displays
# numbers from 10 to 1 on the screen.
# ---------------------------------------------------------

def Display():
    
    for i in range(10, 0, -1):
        print(i, end=" ")

def main():
    Display()

if __name__ == "__main__":
    main()
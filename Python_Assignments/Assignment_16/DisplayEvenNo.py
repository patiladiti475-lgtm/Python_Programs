# ---------------------------------------------------------
# Question:
# Write a program which displays
# first 10 even numbers on the screen.
# ---------------------------------------------------------

def Display():
    
    for i in range(2, 21, 2):
        print(i, end=" ")

def main():
    Display()

if __name__ == "__main__":
    main()
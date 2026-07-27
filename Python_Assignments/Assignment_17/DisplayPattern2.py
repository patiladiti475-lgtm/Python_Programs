# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and
# displays the following pattern.
# Input : 5
# * * * * *
# * * * *
# * * *
# * *
# *
# ---------------------------------------------------------

def Pattern(rows):
    
    for row in range(rows, 0, -1):
        for column in range(row):
            print("*", end="\t")
        print()

def main():
    rows = int(input("Enter number of rows : "))

    Pattern(rows)

if __name__ == "__main__":
    main()
# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and
# displays the following pattern.
# Input : 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ---------------------------------------------------------

def Pattern(rows):
    
    for row in range(1, rows + 1):
        for column in range(1, row + 1):
            print(column, end="\t")
        print()

def main():
    rows = int(input("Enter number of rows : "))

    Pattern(rows)

if __name__ == "__main__":
    main()
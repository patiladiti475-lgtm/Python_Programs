# ---------------------------------------------------------
# Question:
# Write a program which accepts one number and display below pattern 
# Input : 5
#   *    *    *    *    *
#   *    *    *    *    *
#   *    *    *    *    *
#   *    *    *    *    *
#   *    *    *    *    * 
# ---------------------------------------------------------

def Display(rows):
    
    for i in range(rows):
        for i in range(rows):
            print("*", end="\t")
        print()

def main():
    rows = int(input("Enter number of rows : "))

    Display(rows)

if __name__ == "__main__":
    main()
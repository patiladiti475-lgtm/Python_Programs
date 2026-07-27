import os

def main():
    for FolderName , subfolder, filename in os.walk("Marvellous"):
        print("folder Name :", FolderName)
        
        for subf in subfolder:
            print("subfolder name:", subf)




if __name__ == '__main__':
    main()
    
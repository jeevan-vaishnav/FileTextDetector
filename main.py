import os


def isProgrammer(filename):
    with open(filename, 'r') as f:
        fileContent = f.read()

    # Detect all forms of Programmer like Programmer
    if "programmer" in fileContent.lower():
        return True
    else:

        return False


if __name__ == "__main__":

    # Write the concefts of this folder
    dir_contents = os.listdir()
    nProgrammer = 0
    # for each text file, run isProgrammer for item
    for item in dir_contents:
        if item.endswith('txt'):
            print(f" Detecting Programmer is  {item}")
            flag = isProgrammer(item)

            if flag:
                print(f"!!!!!!!! [Programmer found in item {item}]!!!!!!!!!!!")
                nProgrammer += 1
            else:
                print(f" [Programmer not found in file {item}]")

    print("*********Programmer Detector Summary*********")
    print(f"{nProgrammer} files found with Programmer hidden into them")

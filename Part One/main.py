def input_usr(str):
    isCorrect = False
    while isCorrect != True:
        pos = input(str + "\n")
        if (len(str) == 12):
            x = 11
        if (len(str) == 10):
            x = 9
        if (len(pos) >= x):
            print("Please select a correct coin :")
        else:
            chars = list(str)
            if chars[len(pos)] != '-':
                if chars[len(pos) + 1] != '-':
                    isCorrect = True
    return len(pos)

def input_first(str, pos):
    inpt = input("Do you want to add it at the beginning or the end ? (B/E) : ")
    chars = list(str)
    c = chars[pos] + chars[pos + 1]
    chars[pos] = '-'
    chars[pos + 1] = '-'
    if (inpt == "B"):
        str = c + "".join(chars)
    if(inpt == "E"):
        str = "".join(chars) + c
    return str

def change_position(str, pos):
    rm = find_empty(str)
    chars = list(str)
    c1 = chars[pos]
    c2 = chars[pos + 1]
    chars[pos] = '-'
    chars[pos + 1] = '-'
    chars[rm] = c1
    chars[rm + 1] = c2
    str = "".join(chars)
    return str

def find_empty(str):
    chars = list(str)
    for x in range(0, len(str)):
        if chars[x] == '-':
            return x

def check_victory(str):
    if str == "HTHTHTHTHT--":
        return True
    if str == "--HTHTHTHTHT":
        return True
    return False

def main():

    str = "HHHHHTTTTT"
    ct = 0
    while True:
        if ct >= 5:
            print(str)
            if check_victory(str):
                print("You win !")
                return
            else:
                print("You lose !")
                return
        if check_victory(str):
            print("You win !")
            return
        pos = input_usr(str)
        if (len(str) == 10):
            str = input_first(str, pos)
        else:
            str = change_position(str, pos)
        ct = ct + 1

if __name__ == "__main__":
    main()

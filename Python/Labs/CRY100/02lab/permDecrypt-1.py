#!/usr/bin/python3


# DECRYPT:
# 1. DeterminE grid size
def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)
            # if
        # for
    # for
    return num_loc


def keyword_num_assign(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kywrd_num_list = list(range(len(key)))
    # print(kywrdNumList)
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init
            # if
        # inner for
    # for
    return kywrd_num_list



def cipher_decryption():
    msg = input("Enter Cipher Text: ").replace(" ", "").upper()
    # print(msg)
    key = input("Enter keyword: ").upper()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    num_of_rows = int(len(msg) / len(key))

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # decipher
    plain_text = ""
    k = 0
    itr = 0

    # print(arr[6][4])
    # itr = len(msg)

    for i in range(len(msg)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = msg[itr]
            # print("j: {} d: {} m: {} l: {} ". format(j, d, msg[l], l))
            itr += 1
        if itr == len(msg):
            break
        k += 1
    print()

    for i in range(num_of_rows):
        for j in range(len(key)):
            plain_text += str(arr[i][j])
        # for
    # for

    print("Plain Text: " + plain_text)


def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("Encryption")
        cipher_encryption()
    elif choice == 2:
        print("Decryption")
        cipher_decryption()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()

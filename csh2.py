import hashlib


def doMD5hash(my_string):
    h = hashlib.md5()

    h.update(my_string.encode('utf-8'))

    return h.hexdigest()


if __name__ == '__main__':

    # This makes the dictionary

    dictionary = {}

    # read the files

    file = open('hash.txt', 'r')

    hashes = file.readlines()

    file.close()

    file = open('uid.txt', 'r')

    uids = file.readlines()

    file.close()

    # stores values in dictionary

    for i in range(len(hashes)):
        uid = uids[i].strip()

        uids[i] = uid

        hashVal = hashes[i].strip()

        dictionary[uid] = hashVal

    # 1st part

    uid = '001'

    password = '0599'

    salt = '054'

    hashedPass = doMD5hash(password + salt)

    if (dictionary[uid] == hashedPass):

        print('Correct Password and Salt Value.')

    else:

        print('Incorrect Password and Salt.')

    # 2nd part

    finalPasswords = {}

    passwords = ['0' * (4 - len(str(x))) + str(x) for x in range(0, 1001)]

    salts = ['0' * (3 - len(str(x))) + str(x) for x in range(0, 101)]

    for i in uids:

        hashPass = dictionary[i]

        for j in passwords:

            flag = 0

            for k in salts:

                hashGen = doMD5hash(j + k)

                if (hashGen == hashPass):
                    finalPasswords[i] = [hashPass, j, k]

                    flag = 1

                    break

            if (flag == 1):
                break

    print('[ UID\t\tHashed Password\t\t\tPassword\tSalt ]')

    for i in uids:
        detail = finalPasswords[i]

        print("['{}'\t'{}'\t'{}'\t\t'{}']".format(i, detail[0], detail[1], detail[2]))

    # 3rd part

    iD = input('Please enter Username:')

    pS = input('Please enter Password:')

    print(iD, pS)

    salt = finalPasswords[iD][2]

    hashVal = doMD5hash(pS + salt)

    if (hashVal == finalPasswords[iD][0]):

        print('The input password and salt matches the hash value in database.')

    else:

        print('The input password and salt does not match the hash value in database.')
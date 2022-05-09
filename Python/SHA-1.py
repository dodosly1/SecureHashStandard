import functions as func
import preprocessing as pre
import textwrap


def Hash_Initial():
    H0 = "67452301"
    H1 = "efcdab89"
    H2 = "98badcfe"
    H3 = "10325476"
    H4 = "c3d2e1f0"
    num_of_bits = 32
    scale = 16
    H = [H0, H1, H2, H3, H4]
    for hash_value in H:
        H[H.index(hash_value)] = bin(int(hash_value, 16))[2:].zfill(num_of_bits)
    return H


def Create_Constants():
    K = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]
    L = len(K)
    scale = 16
    num_of_bits = 32
    for i in range(L):
        K[i] = bin(K[i])[2:].zfill(num_of_bits)
    return K


def Create_words(M):
    N = len(M)
    W = list()
    length_of_word = 32
    for i in range(N):
        W.append(textwrap.wrap(M[i], length_of_word))
    return W


def Prepare_Schedule(M):
    W1 = Create_words(M)
    N = len(W1)
    for i in range(N):
        for t in range(80):
            if t < 16:
                W1[i][t] = W1[i][t]
            else:
                w1 = int(W1[i][t - 3], 2)
                w2 = int(W1[i][t - 8], 2)
                w3 = int(W1[i][t - 14], 2)
                w4 = int(W1[i][t - 16], 2)
                res1 = w1 ^ w2 ^ w3 ^ w4
                res1 = '{:032b}'.format(res1)
                res1 = func.ROTL(res1, 1)
                W1[i].insert(t, res1)
    return W1


def Hash_Computation(M):
    H_Initial = Hash_Initial()
    W = Prepare_Schedule(M)
    L = len(W)
    K = Create_Constants()
    hash_str = ""
    f = "00000000000000000000000000000000"
    k = "00000000000000000000000000000000"
    for i in range(0, L):
        [a, b, c, d, e] = H_Initial
        for t in range(80):
            print("Calculation for {}th W".format(t))
            print("W{} : {} \n".format(t, W[i][t]))
            print("a : {} ".format(hex(int(a, 2))[2:]))
            print("b : {} ".format(hex(int(b, 2))[2:]))
            print("c : {} ".format(hex(int(c, 2))[2:]))
            print("d : {} ".format(hex(int(d, 2))[2:]))
            print("e : {} ".format(hex(int(e, 2))[2:]))
            if 0 <= t <= 19:
                f = (int(b, 2) & int(c, 2)) | (~int(b, 2) & int(d, 2))
                k = K[0]
            elif 20 <= t <= 39:
                f = int(b, 2) ^ int(c, 2) ^ int(d, 2)
                k = K[1]
            elif 40 <= t <= 59:
                f = (int(b, 2) & int(c, 2)) | (int(b, 2) & int(d, 2)) | (int(c, 2) & int(d, 2))
                k = K[2]
            elif 60 <= t <= 79:
                f = int(b, 2) ^ int(c, 2) ^ int(d, 2)
                k = K[3]
            temp = (int(func.ROTL(a, 5), 2) + f + int(e, 2) + int(k, 2) + int(W[i][t], 2)) % (2 ** 32)
            e = d
            d = c
            c = func.ROTL(b, 30)
            b = a
            a = temp
            a = '{:032b}'.format(a)
            print("Temp : {} \n".format(hex(int(a, 2))[2:]))
        H_Initial[0] = (int(a, 2) + int(H_Initial[0], 2)) % (2 ** 32)
        H_Initial[1] = (int(b, 2) + int(H_Initial[1], 2)) % (2 ** 32)
        H_Initial[2] = (int(c, 2) + int(H_Initial[2], 2)) % (2 ** 32)
        H_Initial[3] = (int(d, 2) + int(H_Initial[3], 2)) % (2 ** 32)
        H_Initial[4] = (int(e, 2) + int(H_Initial[4], 2)) % (2 ** 32)

        for j in range(5):
            H_Initial[j] = '{:032b}'.format(H_Initial[j])
    for hash_value in H_Initial:
        hash_str += hex(int(hash_value, 2))[2:].zfill(8)

    return hash_str


string_to_hash = 'dodos'
print("String to be hashed: {}\n".format(string_to_hash))
Message = pre.Preprocessing(string_to_hash)
print(Message)
H = Hash_Computation(Message)
print("Hashed Message: {}".format(H))

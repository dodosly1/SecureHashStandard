import functions as func
import preprocessing as pre
import textwrap


def Hash_Initial():
    H0 = "6a09e667"
    H1 = "bb67ae85"
    H2 = "3c6ef372"
    H3 = "a54ff53a"
    H4 = "510e527f"
    H5 = "9b05688c"
    H6 = "1f83d9ab"
    H7 = "5be0cd19"
    num_of_bits = 32
    scale = 16
    H = [H0, H1, H2, H3, H4, H5, H6, H7]
    for hash_value in H:
        H[H.index(hash_value)] = bin(int(hash_value, 16))[2:].zfill(num_of_bits)
    return H


def Create_Constants():
    K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
         0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
         0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
         0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
         0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
         0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
         0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
         0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
         0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
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
        for t in range(64):
            if t < 16:
                W1[i][t] = W1[i][t]
            else:
                w1 = int(func.sigma256_1(W1[i][t - 2]), 2)
                w2 = int(W1[i][t - 7], 2)
                w3 = int(func.sigma256_0(W1[i][t - 15]), 2)
                w4 = int(W1[i][t - 16], 2)
                sum1 = (w1 + w2) % (2 ** 32)
                sum2 = (w3 + w4) % (2 ** 32)
                sum3 = (sum1 + sum2) % (2 ** 32)
                sum3 = '{:032b}'.format(sum3)
                W1[i].insert(t, sum3)
    return W1


def Hash_Computation(M):
    H_Initial = Hash_Initial()
    W = Prepare_Schedule(M)
    print(W)
    K = Create_Constants()
    L = len(W)
    hash_str = ""
    for i in range(0, L):
        [a, b, c, d, e, f, g, h] = H_Initial
        for t in range(64):
            w1 = int(func.Sigma256_1(e), 2)
            w2 = int(func.Ch(e, f, g), 2)
            w3 = int(W[i][t], 2)
            T2_1 = int(func.Sigma256_0(a), 2)
            T2_2 = int(func.Maj(a, b, c), 2)
            K_val = int(K[t], 2)
            E_1 = int(d, 2)
            T1 = (w1 + w2 + int(h, 2) + K_val + w3) % (2 ** 32)
            T2 = (T2_1 + T2_2) % (2 ** 32)
            h = g
            g = f
            f = e
            e = (E_1 + T1) % (2 ** 32)
            e = '{:032b}'.format(e)
            d = c
            c = b
            b = a
            a = (T1 + T2) % (2 ** 32)
            a = '{:032b}'.format(a)

        H_Initial[0] = (int(a, 2) + int(H_Initial[0], 2)) % (2 ** 32)
        H_Initial[1] = (int(b, 2) + int(H_Initial[1], 2)) % (2 ** 32)
        H_Initial[2] = (int(c, 2) + int(H_Initial[2], 2)) % (2 ** 32)
        H_Initial[3] = (int(d, 2) + int(H_Initial[3], 2)) % (2 ** 32)
        H_Initial[4] = (int(e, 2) + int(H_Initial[4], 2)) % (2 ** 32)
        H_Initial[5] = (int(f, 2) + int(H_Initial[5], 2)) % (2 ** 32)
        H_Initial[6] = (int(g, 2) + int(H_Initial[6], 2)) % (2 ** 32)
        H_Initial[7] = (int(h, 2) + int(H_Initial[7], 2)) % (2 ** 32)

        for j in range(8):
            H_Initial[j] = '{:032b}'.format(H_Initial[j])
    for hash_value in H_Initial:
        hash_str += hex(int(hash_value, 2))[2:].zfill(8)

    return hash_str


String_to_Hash = "dodos"
String_to_Hash2 = "andriana"
Message = pre.Preprocessing(String_to_Hash2)
H = Hash_Computation(Message)
print("Hashed value: {}".format(H))

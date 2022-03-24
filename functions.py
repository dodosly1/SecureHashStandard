# Python code which implements sha-1 functions
# Antonis Lykourinas

# Functions that operate in 32-bit words
def Ch(x, y, z):
    L = len(x)
    x = int(x, 2)
    y = int(y, 2)
    z = int(z, 2)
    string = "0{}b".format(L)
    result = (x & y) ^ (~x & z)
    result = format(result, string)
    return result


def Maj(x, y, z):
    L = len(x)
    x = int(x, 2)
    y = int(y, 2)
    z = int(z, 2)
    string = "0{}b".format(L)
    result = (x & y) ^ (x & z) ^ (y & z)
    result = format(result, string)
    return result


def Sigma256_0(x):
    L = len(x)
    a = ROTR(x, 2)
    a = int(a, 2)
    b = ROTR(x, 13)
    b = int(b, 2)
    c = ROTR(x, 22)
    c = int(c, 2)
    string = "0{}b".format(L)
    res = a ^ b ^ c
    res = format(res, string)
    return res


def Sigma256_1(x):
    L = len(x)
    a = ROTR(x, 6)
    a = int(a, 2)
    b = ROTR(x, 11)
    b = int(b, 2)
    c = ROTR(x, 25)
    c = int(c, 2)
    string = "0{}b".format(L)
    res = a ^ b ^ c
    res = format(res, string)
    return res


def sigma256_0(x):
    L = len(x)
    a = ROTR(x, 7)
    a = int(a, 2)
    b = ROTR(x, 18)
    b = int(b, 2)
    c = SHR(x, 3)
    c = int(c, 2)
    string = "0{}b".format(L)
    res = a ^ b ^ c
    res = format(res, string)
    return res


def sigma256_1(x):
    L = len(x)
    a = ROTR(x, 17)
    a = int(a, 2)
    b = ROTR(x, 19)
    b = int(b, 2)
    c = SHR(x, 10)
    c = int(c, 2)
    string = "0{}b".format(L)
    res = a ^ b ^ c
    res = format(res, string)
    return res


# functions that operate on a single 32-bit word
# ROTR circular rotation of a number for n elements where n <= len(X)=L
def ROTR(x, n):
    L = len(x)
    return x[L - n:L] + x[0:L - n]


def ROTL(x, n):
    L = len(x)
    return x[n:L] + x[0:n]


# Simple Rotation that zeros the elements from MSB to n
def SHR(x, n):
    L = len(x)
    res = x[0:L - n].rjust(L, '0')
    return res


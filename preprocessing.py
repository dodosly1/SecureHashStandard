# Python script that preprocesses the message for SHA-1 hashing
# Create a list of packages to be processed by the SHA-1 Algorithm
def chuncker(string, byte_length):
    chunked = []
    for b in range(0, len(string), byte_length):
        chunked.append(string[b:b + byte_length])
    return chunked


def Preprocessing(M):
    M = ASCII(M)
    length = len(M)
    message_len = bin(length)[2:].zfill(64)
    if length < 448:
        M = M.ljust(length + 1, '1')
        M = M.ljust(448, '0')
        M = M + message_len
        return [M]
    elif 448 <= length <= 512:
        M = M.ljust(length + 1, '1')
        M = M.ljust(960, '0')
        M = M + message_len
        return chuncker(M, 512)
    else:
        M = M.ljust(length + 1, '1')
        length = length + 1
        while (length % 512) != 0:
            M = M.ljust(length + 1, '0')
            length += 1
        length = length+1
        M = M[0:length-65] + message_len
    return chuncker(M, 512)


# Returns the ASCII binary code of the input message

def ASCII(M):
    string = str()
    values = list(bytes(M, 'ascii'))
    for value in values:
        val = bin(value).replace("0b", "0")
        string += str(val)
    return string


#String_to_Hash = "dodos"
#String_to_Hash2 = "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
#Message = Preprocessing(String_to_Hash2)
#print(Message)
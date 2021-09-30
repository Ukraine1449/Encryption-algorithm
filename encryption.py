def getSeed(passed):
    first = "AaBbCcDdEeFfGgHhIiJjKkLlMm"
    second = "NnOoPpQqRrSsTt"
    third = "UuVvWw"
    num = 0
    for i in passed:
        if first.__contains__(i):
            num = num + 28
        elif second.__contains__(i):
            num = num + 500
        elif third.__contains__(i):
            num = num + 69
        else:
            num = num + 64
    return num

def antiPop(list):
    tbr = list[0]
    list.remove(list[0])
    return tbr

def encrypt(key, message):
    keylist = []
    for i in key:
        keylist.append(i)
    mult = getSeed(keylist)
    messagelist = []
    toreturn = []
    A = 846
    B = 30
    C = 470
    D = 476
    E = 323
    F = 740
    G = 419
    H = 485
    I = 84
    J = 165
    K = 620
    L = 245
    M = 957
    N = 331
    O = 889
    P = 329
    Q = 244
    R = 428
    S = 494
    T = 276
    U = 37
    V = 133
    W = 595
    X = 227
    Y = 792
    Z = 118
    SP = 69
    for i in message:
        messagelist.append(i)
    for i in messagelist:
        if i.lower() == "a":
            toreturn.append(A * mult)
        elif i.lower() == "b":
            toreturn.append(B * mult)
        elif i.lower() == "c":
            toreturn.append(C * mult)
        elif i.lower() == "d":
            toreturn.append(D * mult)
        elif i.lower() == "e":
            toreturn.append(E * mult)
        elif i.lower() == "f":
            toreturn.append(F * mult)
        elif i.lower() == "g":
            toreturn.append(G * mult)
        elif i.lower() == "h":
            toreturn.append(H * mult)
        elif i.lower() == "i":
            toreturn.append(I * mult)
        elif i.lower() == "j":
            toreturn.append(J * mult)
        elif i.lower() == "k":
            toreturn.append(K * mult)
        elif i.lower() == "l":
            toreturn.append(L * mult)
        elif i.lower() == "m":
            toreturn.append(M * mult)
        elif i.lower() == "n":
            toreturn.append(N * mult)
        elif i.lower() == "o":
            toreturn.append(O * mult)
        elif i.lower() == "p":
            toreturn.append(P * mult)
        elif i.lower() == "q":
            toreturn.append(Q * mult)
        elif i.lower() == "r":
            toreturn.append(R * mult)
        elif i.lower() == "s":
            toreturn.append(S * mult)
        elif i.lower() == "t":
            toreturn.append(T * mult)
        elif i.lower() == "u":
            toreturn.append(U * mult)
        elif i.lower() == "v":
            toreturn.append(V * mult)
        elif i.lower() == "w":
            toreturn.append(W * mult)
        elif i.lower() == "x":
            toreturn.append(X * mult)
        elif i.lower() == "y":
            toreturn.append(Y * mult)
        elif i.lower() == "z":
            toreturn.append(Z * mult)
        elif i == " ":
            toreturn.append(SP * mult)
    toreturn.append(mult)
    print(toreturn)
    return toreturn

def decrypt(message):
    A = 846
    B = 30
    C = 470
    D = 476
    E = 323
    F = 740
    G = 419
    H = 485
    I = 84
    J = 165
    K = 620
    L = 245
    M = 957
    N = 331
    O = 889
    P = 329
    Q = 244
    R = 428
    S = 494
    T = 276
    U = 37
    V = 133
    W = 595
    X = 227
    Y = 792
    Z = 118
    SP = 69
    tbr = ""
    mult = message.pop()
    for i in range(len(message)):
        numu = antiPop(message)
        num = numu/mult
        if num == A:
            tbr = tbr + "a"
        elif num == B:
            tbr = tbr + "b"
        elif num == C:
            tbr = tbr + "C"
        elif num == D:
            tbr = tbr + "d"
        elif num == E:
            tbr = tbr + "e"
        elif num == F:
            tbr = tbr + "f"
        elif num == G:
            tbr = tbr + "g"
        elif num == H:
            tbr = tbr + "h"
        elif num == I:
            tbr = tbr + "i"
        elif num == J:
            tbr = tbr + "j"
        elif num == K:
            tbr = tbr + "k"
        elif num == L:
            tbr = tbr + "l"
        elif num == M:
            tbr = tbr + "m"
        elif num == N:
            tbr = tbr + "n"
        elif num == O:
            tbr = tbr + "o"
        elif num == P:
            tbr = tbr + "p"
        elif num == Q:
            tbr = tbr + "q"
        elif num == R:
            tbr = tbr + "r"
        elif num == S:
            tbr = tbr + "s"
        elif num == T:
            tbr = tbr + "t"
        elif num == U:
            tbr = tbr + "u"
        elif num == V:
            tbr = tbr + "v"
        elif num == W:
            tbr = tbr + "w"
        elif num == X:
            tbr = tbr + "x"
        elif num == Y:
            tbr = tbr + "y"
        elif num == Z:
            tbr = tbr + "z"
        elif num == SP:
            tbr = tbr + " "
    return tbr



#Yes ik about fucking dictionaries. Fuck off anyone reading this before i rework it.
# To do is add more chars and dicts



#print(encrypt("tEUhdy2zVYiE", "I like beans"))
encrypt("tEUhdy2zVYiE", "I like beans")

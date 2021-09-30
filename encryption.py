def getSeed(passed):
    first = "AaBbCcDdEeFfGgHhIiJjKkLlMm"
    num = 0
    for i in passed:
        if first.__contains__(i):
            num = num + 70
        else:
            num = num + 90
    return num


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
            toreturn.append("-")
        elif i.lower() == "b":
            toreturn.append(B * mult)
            toreturn.append("-")
        elif i.lower() == "c":
            toreturn.append(C * mult)
            toreturn.append("-")
        elif i.lower() == "d":
            toreturn.append(D * mult)
            toreturn.append("-")
        elif i.lower() == "e":
            toreturn.append(E * mult)
            toreturn.append("-")
        elif i.lower() == "f":
            toreturn.append(F * mult)
            toreturn.append("-")
        elif i.lower() == "g":
            toreturn.append(G * mult)
            toreturn.append("-")
        elif i.lower() == "h":
            toreturn.append(H * mult)
            toreturn.append("-")
        elif i.lower() == "i":
            toreturn.append(I * mult)
            toreturn.append("-")
        elif i.lower() == "j":
            toreturn.append(J * mult)
            toreturn.append("-")
        elif i.lower() == "k":
            toreturn.append(K * mult)
            toreturn.append("-")
        elif i.lower() == "l":
            toreturn.append(L * mult)
            toreturn.append("-")
        elif i.lower() == "m":
            toreturn.append(M * mult)
            toreturn.append("-")
        elif i.lower() == "n":
            toreturn.append(N * mult)
            toreturn.append("-")
        elif i.lower() == "o":
            toreturn.append(O * mult)
            toreturn.append("-")
        elif i.lower() == "p":
            toreturn.append(P * mult)
            toreturn.append("-")
        elif i.lower() == "q":
            toreturn.append(Q * mult)
            toreturn.append("-")
        elif i.lower() == "r":
            toreturn.append(R * mult)
            toreturn.append("-")
        elif i.lower() == "s":
            toreturn.append(S * mult)
            toreturn.append("-")
        elif i.lower() == "t":
            toreturn.append(T * mult)
            toreturn.append("-")
        elif i.lower() == "u":
            toreturn.append(U * mult)
            toreturn.append("-")
        elif i.lower() == "v":
            toreturn.append(V * mult)
            toreturn.append("-")
        elif i.lower() == "w":
            toreturn.append(W * mult)
            toreturn.append("-")
        elif i.lower() == "x":
            toreturn.append(X * mult)
            toreturn.append("-")
        elif i.lower() == "y":
            toreturn.append(Y * mult)
            toreturn.append("-")
        elif i.lower() == "z":
            toreturn.append(Z * mult)
            toreturn.append("-")
        elif i == " ":
            toreturn.append(SP * mult)
            toreturn.append("-")
    toreturn.append(mult)
    print(toreturn)
    return toreturn


#print(encrypt("tEUhdy2zVYiE", "I like beans"))
encrypt("tEUhdy2zVYiE", "I like beans")
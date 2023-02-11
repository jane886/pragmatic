def ensure(con1, con2, message):
    if isinstance(con2, list):
        if len(con1) == len(con2):
            for i, e in enumerate(con2):
                if e != con1[i]:
                    print(message)
                    break
        else:
            print(message)
    elif con1 != con2:
        print(message)

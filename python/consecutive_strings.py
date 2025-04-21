def longest_consec(strarr, k):
    long = max([len(i) for i in strarr])
    second = [i for i in strarr]
    print(long)
    print(second)
        

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
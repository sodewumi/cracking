# ------- Question: 1.1 ------- #

def is_unique_one(astr):
    if len(set(astr)) == len(astr):
        return True
    return False

def is_unique_two(astr):
    unique = True
    arr = list(astr)

    for i in range(len(arr)):
        for j in range(1+i, len(arr)):
            if astr[i] == astr[j]:
                unique = False
    return unique

# ------- Question: 1.2 ------- #
# not in place

def reverse_str_one(astr):
    return astr[::-1]

def reverse_str_two(astr):
    arr = list(astr)
    return "".join([arr[c] for c in range(len(arr)-1,-1,-1)])

# ------- Question: 1.3 ------- #

# ------- Question: 1.4 ------- #
# not in place
def change_char(astr):
    # split strips all white space
    arr = astr.split()
    return "%20".join(arr)

# in place
def change_char_in_place(astr):
    arr = [c for c in astr]
    for i in range(len(arr)):
        if arr[i] == " ":
            arr[i] = "%20"
    return "".join(arr)

# ------- Question: 1.5 ------- #

def is_unique(astr):
    arr = [c for c in astr]
    previous_str = arr[0]
    count = 0
    comp = []
    for ltr in arr:
        if ltr == previous_str:
            count += 1
        else:
            comp.extend([str(count), previous_str])
            count = 1
            previous_str = ltr
    comp.extend([str(count), previous_str])

    if len(comp) < len(astr):
        return "".join(comp)
    else:
        return astr

print(is_unique_one("helo"))
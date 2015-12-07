def is_it_nice(s):
    vowels = "aeiou"
    vowels_count = 0
    if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
        return False

    if "aa" in s or "bb" in s or "cc" in s or "dd" in s or "ee" in s \
       or "ff" in s or "gg" in s or "hh" in s or "ii" in s or "jj" in s \
       or "kk" in s or "ll" in s or "mm" in s or "nn" in s or "oo" in s \
       or "pp" in s or "qq" in s or "rr" in s or "ss" in s or "tt" in s \
       or "uu" in s or "vv" in s or "ww" in s or "xx" in s or "yy" in s or "zz" in s:
        pass
    else:
        return False

    for vowel in vowels:
        vowels_count += s.count(vowel)
    if vowels_count > 2:
        return True
    else:
        return False

result = 0
file = open("day5.txt", "r")
for line in file:
    if is_it_nice(line) == True:
        result += 1

file.close()
print str("We have %s nice words" % result)
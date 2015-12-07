import hashlib

first_part = "ckczppom"

for n in range(0, 99999999):
    md5hash = hashlib.md5()
    md5hash.update(first_part + str(n))
    if md5hash.hexdigest()[0:5] == "00000":
        print str("The secret number is %s" % n)
        break

for n in range(0, 99999999):
    md5hash = hashlib.md5()
    md5hash.update(first_part + str(n))
    if md5hash.hexdigest()[0:6] == "000000":
        print str("The secret number is %s" % n)
        break

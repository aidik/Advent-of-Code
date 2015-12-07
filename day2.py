class box(object):
    def __init__(self, s):
        sizes = s.split("x")
        sizes = map(int, sizes)
        sizes.sort()
        self.h = sizes[0]
        self.l = sizes[1]
        self.w = sizes[2]

    def wrapping_paper(self):
        return (3*self.h*self.l + 2*self.l*self.w + 2*self.w*self.h)

    def ribbon(self):
        return (self.w*self.h*self.l + 2*self.h + 2*self.l)


paper = 0
ribbon = 0
file = open("day2.txt", "r")
for line in file:
    krabice = box(line)
    paper += krabice.wrapping_paper()
    ribbon += krabice.ribbon()

file.close()
print str("We need %s square feet of Paper" % paper)
print str("We need %s feet of Ribbon" % ribbon)
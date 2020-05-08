class student(object):
    def __init__(self, name, score):
        self.a = name
        self.b = score

    def print_score(self):
        print("%s = %s" %(self.a,self.b))

    def get_grade(self):
        if self.b > 90:
            return "A"
        elif self.b > 60:
            return "B"
        else:
            return "C"
    def set_grade(self, score):
        if 0<= score <=100:
            self.b = score
        else:
            raise ValueError("oh, NO")


luo = student("luoquan",99)
huang = student("huangjing",70)
wang = student("wenjian",49)


luo.print_score()
# huang.print_score()
# wang.print_score()
# print(luo.a,luo.get_grade())
# print(huang.get_grade())
# print(wang.get_grade())

ha=luo.set_grade(110)
luo.print_score()

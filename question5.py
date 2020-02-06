class time():

    def _init_(self,hr,min):
        self.hr=hr
        self.min=min

    def addtime(self,t1,t2):
        t3=time(0,0)
        #super()._init_(0,0)
        if t1.min+t2.min>60:
            t3.hr=t1.min+t2.min/60
            t3.min=(t1.min+t2.min)%60
        else:
            t3.min = (t1.min + t2.min + t3.min)
        t3.hr=t1.hr+t2.hr+t3.hr
        return t3

    def displaytime(self):
        print("time is ",self.hr," hours and ",self.min," minutes")

    def displayminute(self):
        print("the total minute is ",(self.hr*60)+self.min)

a = time(2,50)
b = time(1,20)
c = time.addtime(a,b)
c.displaytime()
c.displayminute()

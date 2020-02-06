class sumzero():
    def zer(self):
        g=[-2,8,-6,9,15,-10,3,-9,1,7,4]
        a=len(g)
        for i in range(a-2):
            x=list()
            for j in range(i+1,a-1):
                for k in range(j+1,a):
                    sum=g[j]+g[i]+g[k]
                    if sum==0:
                        x.append(g[i])
                        x.append(g[j])
                        x.append(g[k])
                        print("the num with sum zero is: ",x)
y=sumzero()
y.zer()
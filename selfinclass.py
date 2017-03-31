class numberappend:
    def nplus(self,n1,n2):
        print n1+n2
    def nplustest(self):
        print 1-2
    def nqut(self,n1,n2):
        print n1**n2
count=numberappend()
count.nplus(1,2)  
count.nplustest()
count.nqut(1,2)      
print "--------------"
class numberappend:
    x=0
    def nplus(self):
        self.x=self.x+1
        print self.x 
count=numberappend()
count.nplus()   
count.nplus()   
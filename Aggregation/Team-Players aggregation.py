class Player:
    def __init__(self,pn,pa,pc,pm,pw,pr):
        self.pname=pn
        self.page=pa
        self.pcountry=pc
        self.pmatches=pm
        self.pwickets=pw
        self.pruns=pr

class Team:
    def __init__(self,nop):
        self.no_of_players=nop
        self.pl=[]
        for i in range(self.no_of_players):
            pn=input('Enter the player name:')
            pa=int(input('Enter the player age:'))
            pc=input('Enter player country:')
            pm=int(input('Enter the no of matches:'))
            pw=int(input('Enter the no of wickets:'))
            pr=int(input('Enter the no of runs:'))

            pobj=Player(pn,pa,pc,pm,pw,pr)
            self.pl.append(pobj)
    def maxWictaker(self):
        mwto=self.pl[0]
        for p in self.pl:
            if p.pwickets>mwto.pwickets:
                mwto=p
        return mwto.pname
    def maxRunScorer(self):
        mrso=self.pl[0]
        for p in self.pl:
            if p.pruns>mrso.pruns:
                mrso=p
        return mrso.pname
india=Team(2)
india.maxWictaker()
india.maxRunScorer()
            
        

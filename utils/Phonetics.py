class Phonetics:
    def __init__(self):
        self.vocals = 'euioa'
        self.cons = "bcdfghjklmnpqrstvwxyz"
        self.euphonic_cons = 'drptgzfbcsv'
        self.nv, self.nc= 0, 0
        self.sfv, self.sfc = 0, 0
        self.temp = ''

    def alphabet(self):
        '''len word'''
        alph = 'abcdefghijklmnopqrtsuvwxyz'
        alph_shift = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return alph, alph_shift, len(alph)

    def letter_count(self,name)->int:
        '''Количество букв в слове'''
        temp = []
        name=Phonetics().replica(name)
        alph=Phonetics().alphabet()[0]
        for i in range(len(name)):
            for j in range(len(alph)):
                if (name[i] == alph[j]):
                    temp.append(alph.index(alph[j]))
        return sum(temp)
    
            

    def create(self,vc: str) -> tuple[str,int,int]:
        '''return: (a - слово)[0], (nc - кол-во согл)[1], (nv - кол-во гл)[2]'''
        for i in range(len(vc)):
            for j in range(len(self.vocals)):
                if (vc[i] == self.vocals[j]):
                    self.nv += 1
                    break
        for i in range(len(vc)):
            for j in range(len(self.cons)):
                if (vc[i] == self.cons[j]):
                    self.nc += 1
                    break

        return vc, self.nv, self.nc

    def sound(self,vc)->float:
        for i in range(len(vc)):
            for j in range(len(self.euphonic_cons)):
                if (vc[i] == self.euphonic_cons[j]):
                    self.sfc += 0.5
                    break
        return self.sfc

    def replica(self,list)->str: 
        for i in range(len(list)):  
            self.temp += list[i]
        return self.temp

    def math(self,nv,nc):
        Sum_vc: int = nv+nc
        dif_vc: int = nv-nc 
        kff_vc: float = Sum_vc/2 #коэфф
        return Sum_vc, dif_vc, kff_vc


        
        
        

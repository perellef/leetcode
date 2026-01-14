# https://leetcode.com/problems/n-queens-ii/description/

n = 4

class Løsning:
    def __init__(self):
        self.queens = []

        self.kolonner = set()        
        self.rader = set()        
        self.tv_diagonale = set()
        self.hv_diagonale = set()

    def er_ledig(self, rad, kol):
        if rad in self.rader:
            return False
        if kol in self.kolonner:
            return False
        if rad+kol-1 in self.tv_diagonale:
            return False
        if rad-kol in self.hv_diagonale:
            return False
        return True
        
    def legg_til(self, rad, kol):
        self.queens.append((rad, kol))

        self.kolonner.add(kol)      
        self.rader.add(rad)        
        self.tv_diagonale.add(rad+kol-1)
        self.hv_diagonale.add(rad-kol)

    def fjern_siste(self):
        (rad,kol) = self.queens.pop()
        
        self.kolonner.discard(kol)      
        self.rader.discard(rad)        
        self.tv_diagonale.discard(rad+kol-1)
        self.hv_diagonale.discard(rad-kol)

    def fotavtrykk(self):
        return self.queens.copy()


def løsning(n):

    lagrede = []

    l = Løsning()
    def _rek_(i):

        if i == n:
            lagrede.append(l.fotavtrykk())
            return

        for k in range(n):
            if not l.er_ledig(i,k):
                continue
            l.legg_til(i,k)
            _rek_(i+1)
            l.fjern_siste()
    _rek_(0)
    return len(lagrede)
    
print(løsning(n))
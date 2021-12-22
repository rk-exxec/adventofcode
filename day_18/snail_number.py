from __future__ import annotations
import math

class SnailNumber:
    def __init__(self, a=0, b=0, depth=0, side=-1):
        if isinstance(a, SnailNumber):
            a.nesting_depth += 1
            a.parent = self
            a.side = 0
        if isinstance(b, SnailNumber):
            b.nesting_depth += 1
            b.parent = self
            b.side = 1
        self.pair: list[SnailNumber,SnailNumber] = [a,b]
        self._nesting_depth = depth
        self.side = 0
        self.parent: SnailNumber = None

    @staticmethod
    def load_from_text(text:str):
        if not "," in text:
            return int(text)
        content = text[1:-1] # remove brackets
        #find unnested comma
        depth = 0
        comma_idx = 0
        for i,c in enumerate(content):
            if c == "," and depth == 0:
                comma_idx = i
                break
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
        return SnailNumber(
            SnailNumber.load_from_text(content[:comma_idx]),
            SnailNumber.load_from_text(content[comma_idx+1:])
        )

    def __str__(self):
        return "[" + str(self.pair[0]) + "," + str(self.pair[1]) + "]"


    def __add__(self, b):
        return SnailNumber(self, b)

    @property
    def nesting_depth(self):
        return self._nesting_depth

    @nesting_depth.setter
    def nesting_depth(self, value):
        self._nesting_depth = value
        for el in self.pair:
            if isinstance(el, SnailNumber):
                el.nesting_depth = value + 1

        # if self.nesting_depth >= 4:
        #     self.explode()

    def explode(self):
        if self.nesting_depth == 4:
            return [self.pair,[1,1],True]
        expl = [None,[0,0],False]

        if isinstance(self.pair[0], SnailNumber):
            expl = self.pair[0].explode()
            if self.apply_explosion(expl, 1):
                if sum(expl[1]) == 0:
                    return [None,[],True]     
                else:
                    return expl    

        if isinstance(self.pair[1], SnailNumber) and expl[2] is False:
            expl = self.pair[1].explode()
            if self.apply_explosion(expl, 0):
                if sum(expl[1]) == 0:
                    return [None,[],True]     
                else:
                    return expl
    
        return expl

    def apply_explosion(self, expl, side):
        applied = False
        #if self.side == side: return False
        if expl[0] is not None and expl[1][side]:
            if self.nesting_depth == 3:
                self.pair[side-1] = 0
            if isinstance(self.pair[side], int):
                self.pair[side] += expl[0][side]
                expl[1][side] = 0
                applied = True
            elif isinstance(self.pair[side],SnailNumber):
                self.pair[side].add_explosion(expl[0][side], side-1)
                expl[1][side] = 0
                applied = True

        return applied

    def add_explosion(self, value, side):
        if isinstance(self.pair[side], SnailNumber):
            self.pair[side].add_explosion(value, side)
        else:
            self.pair[side] += value

    def split(self):
        for i,el in enumerate(self.pair):
            if isinstance(el, SnailNumber):
                if el.split():
                    return True
            else:
                if el >= 10:
                    self.pair[i] = SnailNumber(math.floor(el/2), math.ceil(el/2), self.nesting_depth+1, side=i)
                    return True
                continue
        return False       

    def reduce(self):
        did_exp = self.explode()[2]
        if did_exp: 
            #print("After explode: ", self)
            return True
        did_spl = self.split()
        if did_spl: 
            #print("After split: ", self)
            return True
        return False

    def magnitude(self):
        magn = 0
        for i,el in enumerate(self.pair):
            if isinstance(el, SnailNumber):
                magn += (3-i)*el.magnitude()
            else:
                magn += (3-i)*el
        return magn

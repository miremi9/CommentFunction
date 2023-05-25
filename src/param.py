SIZE = 74
BORDERSIZE = 6

class Param:
    def __init__(self,size,bordersize,throw_message="throw"):
        self.size = size
        self.bordersize = bordersize
        self.first = "/" + "*"*(size-2)
        self.end = " "+"*"*(size-2) +  "/"
        self.throw_message = throw_message
        self.border = " "+"*"*(bordersize-2)+ " "
        self.nb_tabulation = 0
        self.sizeempty = len(self.first)-2*len(self.border)+1
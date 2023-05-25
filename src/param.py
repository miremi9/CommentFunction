class Param:
    def __init__(self,size,bordersize,throw_message="throw"):
        self.size = size
        self.bordersize = bordersize
        self.first = "/" + "*"*(size)
        self.end = "*"*(size) +  "/"
        self.throw_message = throw_message
        self.border = "*"*(bordersize)
        self.nb_tabulation = 0
        self.sizeempty = size-2*len(self.border)-2
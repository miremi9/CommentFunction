import re
import sys

sys.path.append("src")
import param
import function as fc

SIZE = 74
BORDERSIZE = 6



if __name__ =="__main__":
    nb_arg = len(sys.argv)
    if nb_arg ==1:   #default function
        function2run = fc.rexegtext
    elif (nb_arg == 2):
        param = sys.argv[1]
        if param == "-re":
            function2run = fc.rexegtext
        elif param =="-start":
            function2run = fc.startwrite
        else :
            raise "arg must be -re or -start"
    else:
        print(nb_arg)
        raise "too many arg"
    
    myparam  =param.Param(SIZE,BORDERSIZE,"throw CException otherwise")
    while True:
        out = function2run(myparam)
        if out:
            break
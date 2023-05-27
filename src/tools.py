import re
import data

def definition_traitement(definition:str):

    if m:=re.search('^\s*([^\(\)~ ]+)\(\)', definition):       #constructordefaut
        methode = "Default class Constructor | " + m.group(1)
        args = "None"
        precon = "None"
        postcon = "Attribut of this are initialized"
        output = "None"

    elif m:=re.search('^\s*(~[^\(\) ]+)\(\)', definition):       #destructor
        methode = "Destructor | " + m.group(1)
        args = "None"
        precon = "None"
        postcon = "Attribut of this are deleted"
        output = "None"

    elif m:=re.search('^\s*([^\(\) ]+)\(\s*(.+)\s*\)', definition):   
        if m.group(1) in m.group(2):  #recopie
            methode = "Constructor of Copy | " + m.group(1)
            args = m.group(2)
            nameparam = args.split(" ")[-1]
            precon = f"{nameparam} must be initialized"
            postcon = f"Attribut of this are initialized and it attribut have the same value as {nameparam}"
        else:           #confort
            methode = "Constructor | " + m.group(1)
            args = m.group(2)
            precon = ""
            postcon = "Attribut of this are initialized according to the parameters"
        output = "None"
    

    elif m:=re.search('(.+)\s+([^()]+)\((.*)\)', definition):   #classique function
        methode = m.group(2)
        if m.group(3):
             
           args = m.group(3)
        else:
            args = "None"
        if "void" in m.group(1):
            output  = "None"
        else :
          
            output = m.group(1)
        precon = ""
        postcon = ""

    else:
        raise ValueError
    return data.Function(methode,args,precon,postcon,output)

def finish_definition( fc):
    if not fc.methode:
        fc.methode = input("Nom de fonction : ")
    if not fc.args:
        fc.args = input("Arguments : ")        
    if not fc.precon:
        fc.precon = input("precondition : ")
    if not fc.output:
        fc.output = input("Output : ")
    if not fc.postcon:
        fc.postcon = input("Postcon : ")





def traitement_element(function,myparam):
    function.precon = function.precon.replace("throw",myparam.throw_message)
    function.args = "Input : " + function.args
    function.precon = "precondtion : " +function.precon
    function.postcon = "Postcondition : " + function.postcon
    function.output = "Output : " + function.output

def create_message(function:data.Function,myparam):
    

    nb_tabulation = myparam.nb_tabulation
    sizeempty = myparam.sizeempty
    border = myparam.border
    size = myparam.size
    liste = [function.args,function.precon,function.output,function.postcon]
    start = 0
    lines_message = [myparam.first]
    line = ""
    while len(function.methode[start:])>sizeempty:
        line = border + " "+function.methode[start:start+sizeempty] +" "+ border
        lines_message.append(line)
        start +=sizeempty

    line = border +" " + function.methode[start:].ljust(sizeempty) +" "+border
    lines_message.append(line)

    line = "*"*size
    lines_message.append(line)
    

    for part in liste:
        start = 0
        for line in split_text(part,sizeempty):
            line = border +" " + line[start:].ljust(sizeempty) +" "+border
            lines_message.append(line)
    lines_message.append(myparam.end)
    begin_line = "\n " + "\t" * myparam.nb_tabulation
    message  =f"{begin_line}".join(lines_message)
    return message




def split_text(text:str,size:int) -> list:
    out = [""]
    index = int(0)
    for word in text.split(" "):
        if (len(word) + 1 + len(out[-1])) < size:
            out[-1] += word +" "
        else:
            if len(word)>size:
                raise ValueError("Mot trop grand")
            out.append(word)

    return out

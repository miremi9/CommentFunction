import tools
import data
def rexegtext(myparam):
    definition = input("definition : ")
    try:
        function = tools.definition_traitement(definition)
    except ValueError:
        print("Failed")
        return 1
    tools.finish_definition(function)

    tools.traitement_element(function,myparam)
    message = tools.create_message(function,myparam)

    print("\n\n" +message + "\n\n")
    return 0

def startwrite(myparam):
    function = data.Function()
    tools.finish_definition(function)
    tools.traitement_element(function,myparam)
    message = tools.create_message(function,myparam)
    print("\n\n" +message + "\n\n")
    return 0
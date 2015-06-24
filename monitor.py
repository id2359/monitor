import clips
from dispatch import Dispatcher, DispatchError
from retrievers import RetrievalError

BAD_VALUE = clips.Symbol("bad")

def get_value(name):
    print "get_value: %s" % name
    try:
        value = Retriever().get_value(name)
        print "got value: %s" % value
        return value
    except RetrievalError:
        print "retrieval error!"
        return BAD_VALUE
    except DispatchError:
        print "dispatch error!"
        return BAD_VALUE

if __name__=="__main__":
    clips.RegisterPythonFunction(get_value, "python-get-value")
    clips.Load("rules.clp")
    clips.LoadFacts("initialfacts.clp")
    clips.Run()




import clips
from dispatch import Dispatcher, DispatchError
from retrievers import RetrievalError
import sys

sys.path.append('retrievers')

NULL_VALUE = clips.Symbol("null")

def get_value(name):
    print "get_value: %s" % name
    try:
        value = Dispatcher().get_value(name)
        print "got value: %s" % value
        return clips.Integer(value)
    except RetrievalError:
        print "retrieval error!"
        return NULL_VALUE
    except DispatchError:
        print "dispatch error!"
        return NULL_VALUE
    except Exception, ex:
        print "dispatch err: %s" % ex
        return NULL_VALUE


def python_print(msg):
    print "MON:> %s" % msg

if __name__=="__main__":
    clips.RegisterPythonFunction(get_value, "python-get-value")
    clips.RegisterPythonFunction(python_print, "python-print")
    clips.Load("rules.clp")
    clips.LoadFacts("initialfacts.clp")
    clips.Run()
    clips.SaveFacts("output.clp")

    print "done"

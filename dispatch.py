import inspect
import importlib
import retrievers

class DispatchError(Exception):
    pass

class Dispatcher(object):
    def get_value(self, name):
        print "getting %s" % name
        python_name = name.replace("-","_")
        if hasattr(retrievers, python_name):
            func = getattr(retrievers, python_name)
            return func()
        else:
            raise DispatchError(name)

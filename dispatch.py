import retrievers
import os

class DispatchError(Exception):
    pass

class Dispatcher(object):
    def get_value(self, name):
        python_name = name.replace("-","_")
        if hasattr(retrievers, python_name):
            func = getattr(retrievers, python_name)
            return func()
        elif os.path.exists(name):
            result = float(os.popen(name).read().strip())
            return result
        else:
            raise DispatchError(name)

import inspect
import importlib
import retrievers

class DispatchError(Exception):
    pass


class Dispatcher(object):
    def get_value(self, name):
        python_name = name.replace("-","_")
        for module_name in inspect.get_members(retrievers, inspect.ismodule):
            module = importlib.import_lib(module_name)
            if hasattr(module, python_name):
                func = getattr(module, python_name)
                try:
                    return func()
                except:
                    raise retrievers.RetrievalError(name)
                
        raise DispatchError(name)

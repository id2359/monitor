import retrievers
import os
import json

class DispatchError(Exception):
    pass

class Dispatcher(object):
    TOOLS_FILE = "tools.json"

    def __init__(self):
      if os.path.exists(self.TOOLS_FILE):
         with open(self.TOOLS_FILE) as tf:
            self.tools_dict = json.load(tf)
      else:
         print "no tools.json defined!"
         self.tools_dict = {}

    def get_value(self, name):
        python_name = name.replace("-","_")
        if hasattr(retrievers, python_name):
            func = getattr(retrievers, python_name)
            return func()
        else:
            tool_path = self.get_tool(name)
            if not os.path.exists(tool_path):
               raise DispatchError("tool path %s does not exist" % tool_path)
            
            try:
                result = float(os.popen(tool_path).read().strip())
            except ValueError:
                raise DispatchError(name)
            return result

    def get_tool(self, tool_name):
      try:
         tool_path = self.tools_dict[tool_name]
         return tool_path
      except KeyError:
         raise DispatchError("could not retrieve tool path for tool %s" % tool_name)


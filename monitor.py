import clips

def dispatch(name):
    pass

if __name__=="__main__":
    clips.RegisterPythonFunction(dispatch, "python-get-value")
    clips.Load("rules.clp")
    clips.Load("initialfacts.clp")
    clips.Run()




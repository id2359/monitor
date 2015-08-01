#! /usr/bin/python

import clips
from dispatch import Dispatcher, DispatchError
from retrievers import RetrievalError
import sys
import os
from  datefuncs import *

sys.path.append('./src/retrievers')

NULL_VALUE = clips.Symbol("null")

def get_value(name):
    try:
        value = Dispatcher().get_value(name)
        return clips.Integer(value)
    except RetrievalError, rerr:
        print "retrieval error for %s: %s" % (name, rerr)
        return NULL_VALUE
    except DispatchError, derr:
        print "dispatch error for %s: %s" % (name, derr)
        return NULL_VALUE
    except Exception, ex:
        print "Unexpected error for %s: %s" % (name, ex)
        return NULL_VALUE


def python_print(msg):
    print "MON:> %s" % msg

if __name__=="__main__":
    clips.RegisterPythonFunction(get_value, "python-get-value")
    clips.RegisterPythonFunction(python_print, "python-print")
    clips.RegisterPythonFunction(days, "python-days")
    print "days"
    clips.RegisterPythonFunction(add_days, "python-add-days")
    print "add_days"
    clips.RegisterPythonFunction(add_weeks, "python-add-weeks")
    print "add_weeks"
    clips.RegisterPythonFunction(add_months, "python-add-months")
    print "add_months"
    clips.RegisterPythonFunction(add_years, "python-add-years")
    print "add_years"
    clips.RegisterPythonFunction(today, "python-today")
    print "today"
    clips.RegisterPythonFunction(after, "python-after")
    print "after"

    clips.Load("src/rules.clp")
    print "loaded rules"
    clips.LoadFacts("src/initialfacts.clp")
    print "loaded initial facts"
    if os.path.exists("food.clp"):
        clips.LoadFacts("food.clp")
    if os.path.exists("taplog.clp"):
        clips.LoadFacts("taplog.clp")
    clips.Run()
    print "run completed"
    clips.SaveFacts("output.clp")
    print "saved output"

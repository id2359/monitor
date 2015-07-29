from datetime import datetime, timedelta

month_names = ["jan", "feb", "mar", "apr", "may", "jun", 
               "jul", "aug", "sep", "oct", "nov", "dec"]

def python_date(date_string):
    day, month, year = date_string.split("-")
    m = month_names.index(month.lower()) + 1
    return datetime(int(year), m, int(day))

def date_string(python_date):
    d = python_date.day
    m = python_date.month
    y = python_date.year

    month_name = month_names[m - 1]
    month_name = month_name[0].upper() + month_name[1:]
    return "%s-%s-%s" % (d,month_name, y)

def days(ds1, ds2):
    # 29-Dec-1978  
    # return days between
    a = python_date(ds1)
    b = python_date(ds2)
    c = a - b
    return c.days

def add_days(ds, num_days):
    a = python_date(ds)
    d = timedelta(days=num_days)
    return date_string(a + d)

def add_years(ds,num_years):
    a = python_date(ds)
    d = timedelta(years=num_years)
    return date_string(a + d)

def add_weeks(ds, num_weeks):
    a = python_date(ds)
    w = 7 * num_weeks
    d = timedelta(days=w)
    return date_string(a + d)

def add_months(ds, num_months):
    a = python_date(ds)
    d = timedelta(months=num_months)
    return date_string(a + d)
    
def today():
    a = datetime.datetime.now().date()
    return date_string(a)

def inside(ds, start_ds, finish_ds):
    a = python_date(ds)
    b = python_date(start_ds)
    c = python_date(finish_ds)
    return a >= b and a <= c

def outside(ds, start_ds, finish_ds):
    return not inside(ds, start_ds, finish_ds)

def in_last_days(ds, num_days):
    t = today()
    a = add_days(t, -1 * num_days)
    return inside(ds, a, t)

def after(ds1, ds2):
    return python_date(ds1) > python_date(ds2)


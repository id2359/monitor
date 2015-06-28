class RetrievalError(Exception):
    pass

def max_temp():
    from bs4 import BeautifulSoup

    import re
    url = "http://www.bom.gov.au/wa/forecasts/perth.shtml"
    import urllib2
    try:
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        print soup.title.name
        pattern = re.compile(""".*<em class="max">(.+)</em>.*""")
        m = pattern.match(pattern)
        if m:
            ts= m.groups(1)[0]
            t = int(ts)
            return t
    except Exception, ex:
        print "error getting max_temp: %s" % ex
        raise RetrievalError("%s" % ex)

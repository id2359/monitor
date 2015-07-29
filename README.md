This program does a grab-bag of personal things - the intent is to output a daily "briefing" by monitoring
a weather site and some other logs of my daily activities.

Running runmonitor:

1) Parses the exported data from TapLog and Food Diary ( Two apps on my Android phone) using Rebol.
2) Scrapes some local weather data from the web using Rebol.
3) Emits the parsed and scraped data as a collection of CLIPS facts.
4) Runs a CLIPS rule set over the emitted data - using CLIPS and PyCLIPS ( the latter allows Python functions
   to be registered in CLIPS. I've registered some date manipulation functions mainly.)
   
5) The output is stored as both rebol data and clips facts as well as summarised in the stdout.

rebol []

output-file: %taplog-data.r

reading: make object! [
	date: none
	time: none
	parameter: none
	quantity: none
    clips: does [
        if none? quantity [ quantity: "" ]
        parameter: replace parameter "Symptom," ""
        return rejoin [ "(taplog " date/date " " time " "
                           lowercase replace/all parameter " " "" 
                           " "
                           quantity
                           ")" newline ]
        ]

]


data: []
current: none

emit: func [ blk ][
	switch first blk [
		date [
			if not none? current [
				append  data current
			]
			
			current: make reading [
				date: blk/2
			]
			
		  ] 

		time [ current/time: blk/2 ]
		
		parameter [ current/parameter: blk/2 ]
		
		quantity [ current/quantity: to decimal! replace blk/2 "," ""  ]
	]
]


digit: charset "0123456789"
yearnum: [ 4 digit ]

daynum: monthnum: timenum:  [ digit opt digit ]
datestring: [ d: daynum "/" m: monthnum "/" y: yearnum ( emit reduce ['date to-date rejoin [ d "-" m "-" y ] ] ) ]

spaces: [ any #" " ]
timestring: [ h: timenum #":" m: timenum spaces f: ["AM" | "PM"]
	( either [ f = "AM" ] [
			emit reduce [ 'time to time! rejoin [ h ":" m ]
			]][
			emit reduce [ 'time to time! join [ h + 12 ":" m ] ]
		]
	) 
]


parameter: [ thru #"[" copy inside to #"]" ( emit reduce [ 'parameter inside ])]
quantity: [ thru "(quantity: " copy q to ")" ( emit reduce [ 'quantity q ] ) ]
rule: [
	datestring spaces timestring spaces parameter spaces opt quantity spaces newline  |
	newline
]

lines: read/lines to file! system/script/args
foreach line lines [
	if line [
		parse/all line [ some rule ]
	]
]


save output-file data

clips-file: %taplog.clp
stream: open/new clips-file
foreach thing data [
    append stream thing/clips
]

close stream


rebol []
food-diary-file: to file! system/script/args
lines: read/lines food-diary-file
lines: next lines
blk: []

foreach line lines [
        parts: parse line none
        d: to date! first parts
        parts: next parts
        ;t: to time! first parts
        parts: next parts
        h: lowercase first parts
        parts: next parts
        s: ""
        while [ not tail? parts ][
            s: rejoin [ s  first parts ]
            parts: next parts
        ]
        s: lowercase s
        s: replace s "&" "" 
        b: reduce [ d h s ]
        append/only blk b
    ]

save %food-data.r blk

clips-fact: func [ food date  foodtype ][
    return rejoin [ "(food " food " " {"} date {"}   " " foodtype ")" newline ]
]

clips-file: open/new %food.clp

foreach b blk [
    line: clips-fact b/3 b/1 b/2
    append clips-file line
]

close clips-file




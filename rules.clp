
(deffunction msg (?s)
  (python-call python-print  ?s))

(defrule get-value
	?g <- (need ?x)
	=>
	(bind ?value (python-call python-get-value ?x))
	(if (eq ?value null) then
	  (assert (bad ?x))
	else
	(assert (value ?x ?value))
    (retract ?g)
	))

(defrule keep-trying
	?n <- (need ?x)
	?b <- (bad ?x)
	(policy ?x keeptrying)
	=>
	(retract ?b)
	(retract ?n)
	(assert (need ?x)))
	
(defrule giveup
	?n <- (need ?x)
	?b <- (bad ?x)
	(policy ?x giveup)
	=>
	(retract ?n)
	(retract ?b))



(defrule mild-temperature
   (value max-temp ?t)
   (test (< ?t 20))
   (test (> ?t 15))
   =>
   (assert (mild))
   (msg "wear long sleeved shirt"))

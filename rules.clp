(defrule get-value
	?g <- (need ?x)
	=>
	(bind ?value (python-get-value ?x))
	(if (= ?value null) then
	 	(assert bad ?x)
	else
		(assert (value ?x ?value)))
	(retract ?g))

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
	

	
	
	

	

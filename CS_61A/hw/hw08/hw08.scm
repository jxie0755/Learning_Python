; CS61A HW08


; Q1 Cadr and Caddr


(define (cddr s)
	(cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
	(car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
	(car (cddr s))
)



; Q2 Sign
; Using cond, define a procedure sign that returns -1 for negative arguments, 0 for zero, and 1 for positive arguments


(define (sign x)
  'YOUR-CODE-HERE
	(cond
	((< x 0) -1)
	((> x 0) 1)
	(else 0))
)



; Q3 Pow

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
	(cond
	((= n 0) 1)
	((even? n ) (square (pow b (/ n 2))))
	((odd? n ) ( * (square (pow b (/ (- n 1) 2))) b))
	)
)



; Q4 Ordered

(define (ordered? s)
  'YOUR-CODE-HERE
	(cond
	((null? (cdr s)) #t)
	((< (car s) (cadr s)) (ordered? (cdr s)))
	((= (car s) (cadr s)) (ordered? (cdr s)))
	((> (car s) (cadr s)) #f)
	)
)


; Q5 No Dots!

(define (nodots s)
  'YOUR-CODE-HERE
	(if (null? s)
	nil
	(if (pair? s)
		(if (pair? (car s))
		(cons (nodots (car s)) (nodots (cdr s)))
		(cons (car s) (nodots (cdr s)))
		)
		(cons s nil)
	)
	)
)



; Sets as sorted lists
; Q6 Contains

(define (empty? s) (null? s))

(define (contains? s v)
	(cond
	((empty? s) #f)
	'YOUR-CODE-HERE
	((= (car s) v) #t)
	((> (car s) v) #f)
	(else (contains? (cdr s) v))
	)
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)



; Q7 Add

(define (add s v)
	(cond
	((empty? s) (list v))
	'YOUR-CODE-HERE
	((contains? s v) s)
	((> (car s) v) (cons v s))
	((< (car s) v) (cons (car s) (add (cdr s) v) ))
	)
)



; Q8 Intersect and Union

(define (intersect s t)
	(cond ((or (empty? s) (empty? t)) nil)
    'YOUR-CODE-HERE
    (else nil) ; replace this line
    ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)



(define (union s t)
	(cond ((empty? s) t)
			((empty? t) s)
			'YOUR-CODE-HERE
			(else nil) ; replace this line
			))
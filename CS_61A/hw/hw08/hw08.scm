; CS61A HW08


; Q1 Cadr and Caddr


(define (cddr s)
  (cdr (cdr s)))
(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)



; Q2 Sign
; Using cond, define a procedure sign that returns -1 for negative arguments, 0 for zero, and 1 for positive arguments


(define (sign x)
  (cond
    ((< x 0) -1)
    ((> x 0) 1)
    (else 0))
)



; Q3 Pow

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((even? n) square (pow b n/2))
    ((ood? n)  * (square (pow b (/ (- n 1) 2))) n )
    )
)




(define (ordered? s)
  'YOUR-CODE-HERE
)

(define (nodots s)
  'YOUR-CODE-HERE
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))

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

(define (add s v)
    (cond ((empty? s) (list v))
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))

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
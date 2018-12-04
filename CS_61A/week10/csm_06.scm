; CSM 06 Introduction to Scheme



(define (factorial n)
  (if (= n 0)
    1
    (* n (factorial (- n 1)) )))

; quotient is floor divides, remainder is the rest
(quotient 103 10)
; >>> 10

(remainder 103 10)
; >>> 3


; Q2 Hailstone again
(define (hailstone seed n)
  (if (= n 0)
    seed
    (if (= 0 (remainder seed 2))
      (hailstone
      (quotient seed 2)
      (- n 1)
    )
    (hailstone
    (+ 1 (* seed 3))
    (- n 1)
    )
  )
)


; Q3
; Define well-formed, which determines whether lst is a well-formed list or not.
; Assume that lst only contains numbers.

; well-formed with nested if statements
(define (well-formed lst)
  (if (null? lst)
    #t
    (if (number? lst)
      #f
      (well-formed (cdr lst)))))

; well-formed with a cond statement
(define (well-formed lst)
  (cond ((null? lst) #t)
    ((number? lst) #f)
    (else (well-formed (cdr lst)))))


; Q4
; Define is-prefix, which takes in a list p and a list lst and determines if p is a
prefix of lst

; is-prefix with nested if statements
(define (is-prefix p lst)
  (if (null? p)
    #t
    (if (null? lst)
      #f
    (and
      (= (car p) (car lst))
      (is-prefix (cdr p) (cdr lst))))))

; is-prefix with a cond statement
(define (is-prefix p lst)
  (cond ((null? p) #t)
    ((null? lst) #f)
    (else (and (= (car p) (car lst))
      (is-prefix (cdr p) (cdr lst))))))

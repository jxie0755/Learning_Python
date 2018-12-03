;; Extra Scheme Questions ;;


; Q5 Make a List to be ((1) 2 (3 . 4) 5)
(define lst
  (cons (cons 1 nil) (cons 2 (cons (cons 3 4) (cons 5 nil))))
)


; Q6 Compose
(define (composed f g)
  (lambda (x)(f (g x)))
)


; Q7 Remove
(define (remove item lst)
  (cond
    ((null? lst)nil)
    ((= (car lst) item)(remove item (cdr lst)))
    ((not (= (car lst) item))(cons (car lst)(remove item (cdr lst))))
  )
)


; Q8 Greatest Common Divisor
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))

(define (gcd a b)
  (cond
    ((= a 0) b)
    ((= b 0) a)
    ((= (modulo a b) 0) b)
    ((> a b) (gcd b (modulo a b)))
    ((< a b) (gcd a (modulo b a)))
  )
)


; Q9
(define (in? x lst)
  (cond
    ((null? lst) #f)
    ((= (car lst) x) #t)
    (else (in? x (cdr lst)))
  )
)

(define result nil)
(define (no-repeats s)
  (cond
    ((null? s)nil)
    ((in? (car s) result)(no-repeats (cdr s)))
    (else ((define result (cons (car s) result)) (no-repeats (cdr s))))
  )
)

; Q10
(define (substitute s old new)
  'YOUR-CODE-HERE
)

; Q11
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)
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
(define (in-lst s x)
  (if (null? s)
     #f
     (or (= x (car s)) (in-lst (cdr s) x))))

(define (no-repeats s)
  (if (null? s)
        s
        (if (in-lst (cdr s) (car s))
            (no-repeats (cdr s))
            (cons (car s) (no-repeats (cdr s))))))

; Q10
(define (substitute s old new)
  'YOUR-CODE-HERE
)

; Q11
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)
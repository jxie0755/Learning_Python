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


; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  'YOUR-CODE-HERE
)

; Q10
(define (substitute s old new)
  'YOUR-CODE-HERE
)

; Q11
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)
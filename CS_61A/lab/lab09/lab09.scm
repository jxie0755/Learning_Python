;; Scheme ;;


; Q1 WWSD: List

; scm> (equal? '(1 . (2 . 3)) (list 1 (cons 2 3)))
; >>> #t
; scm> '(1 . (2 . 3))
; >>> (1 2 . 3)
; scm> (list 1 (cons 2 3))
; >>> (1 (2 . 3)) ; list会强行完美造list,加一个nil在最后

; scm> (cons 1 '(list 2 3))
; >>> (1 list 2 3)

; scm> (cons (list 2 (cons 3 4)) nil)
; >>> ((2 (3 . 4)))

; scm> '(cons 4 (cons (cons 6 8) ()))
; >>> (cons 4 (cons (cons 6 8) ()))

; Q2
(define (over-or-under x y)
  'YOUR-CODE-HERE
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

; Q3
(define (filter f lst)
  'YOUR-CODE-HERE
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

; Q4
(define (make-adder num)
  'YOUR-CODE-HERE
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13
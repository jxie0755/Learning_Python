; CS61A Lecture 24 Scheme


; Scheme is a Dialect of Lisp


; Call expressions
; also called combination

(quotient 10 2) ; is 10 / 5, >>>  2

; nest combination
(quotient (+ 8 7) 5) ; >>> 3

; combination can span multiple lines
(+ (* 3
      (+ (* 2 4)      ; >>> 8
         (+ 3 5)))    ; >>> 8 total is 16, 16 * 3 = 48
   (+ (- 10 7)        ; >>> 3
      6))             ; >>> 3+6=9, 9 + 48 = 57


(+ 1 2 3 4)             ; >>> 10
(+)                     ; >>> 0
(*)                     ; >>> 1
(- 12)                  ; >>> -12
(- 20 1 2 3 4 5)        ; >>> 5
(* (* 2 2 2 2 2 3 3) 7) ; >>> 2016
(number? 12)    ; >>> #t
(integer? 3.3)  ; >>> f
(zero? 2)       ; >>> #t



; Definitions

; bind a value
(define pi 3.14)
(* 2 pi) ; >>> 6.28

; define a function
(define (square x) (* x x))
(define (average x y) (/ (+ x y) 2))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (sqrt x)
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (= (square guess) x)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1))

; define a lambda function
; two equivalent expressions:
(define (plus4 x) (+ x 4))
(define plus4 (lambda (x) (+ x 4)))

((lambda (x y z) (+ x y (square z))) 1 2 3)
; >>> 1 + 2 + 3^2 = 12



; List demos

(cons 1 2)                        ; >>> (1 . 2) as a pair, not a well formed list
(cons 1 (cons 2 nil))             ; >>> [1, 2]
(cons 1 (cons 2 (cons 3 4)))      ; >>> [1, 2, (3 . 4)]
(cons (cons 1 2) 2)               ; >>> ((1 . 2) . 2)
(cons (cons 1 2) nil)             ; >>> [(1 . 2)]
(cons (cons 1 (cons 2 nil)) nil)  ; >>> [[1, 2]]
(cons (cons 1 2) (cons 3 nil))    ; >>> [(1 . 2), [3]]

(pair? (cons 1 2))                ; >>> #t
(pair? (cons 1 (cons 2 nil)))     ; >>> #t
(pair? nil)                       ; >>> #f
(null? nil)                       ; >>> #t
(null? (cons 1 2))                ; >>> #f

; easy way to create a linked list as a list
(list 1 2)
(list 1 2 3 4)
(cdr (list 1 2 3 4))  ; >>> (2 3 4)

(define x (cons 1 2))
(list (car x) (cdr x))
(cons (car x) (cons (cdr x) nil))

(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

(define squares (list 1 4 9 16 25))

(length squares)


; Symbolic Programming
(define a 1)
(define b 2)
(list a b)   ; >>> (1 2)
(list 'a 'b) ; >>> (a b)
(list 'a b)  ; >>> (a 2)

(car '(a b c)) ; >>> a
(cdr '(a b c)) ; >>> (b c)



; Sierpinski (Presented in subsequent lecture)

(define (repeat k fn)
  ; Repeat fn k times.
  (if (> k 1)
      (begin (fn) (repeat (- k 1) fn))
      (fn)))

; Star: (repeat 5 (lambda () (begin (fd 100) (rt 144))))

(define (tri fn)
  ; Repeat fn 3 times, each followed by a 120 degree turn.
  (repeat 3 (lambda () (fn) (lt 120))))

(define (sier d k)
  ; Draw three legs of Sierpinski's triangle to depth d.
  (tri (lambda ()
         (if (= k 1) (fd d) (leg d k)))))

(define (leg d k)
  ; Draw one leg of Sierpinski's triangle to depth d.
  (sier (/ d 2) (- k 1))
  (penup) (fd d) (pendown))

(sier 400 6)

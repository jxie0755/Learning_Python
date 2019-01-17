;; CS61A Lecture 28 Tail Calls

;; Dynamic scope vs. Lexical scope

Lexical: Python and Scheme - The parent of a frame is the environment in which a procedure was defined
Dynamic: The parent of a frame is the environment in which a procedure was called.

; Example
(define f(lambda (x) (+ x y)))
(define g (lambda (x y) (f (+ x x))))
(g 3 7)

; Lexical:
; (g 3 7) == f(6) == 6 + y
; parent for f's fram is the global - causing error as y in f is unknown

; Dynamic:
; (g 3 7) == f(6) == 6 + y, y is in frame g, which y = 7, therefore f(6) == (6 + 7) == 13

;; Tail recursion

; functional programming
; 1. All functions are pure functions (no side effect)
; 2. No re-assignment and no mutable data types
; 3. Name-value bidnings are permanent

; Advantage:
; 1. The value of an expression is independent of the order in which sub-expressions are evaluated
; 2. Sub-expression can safely be evaluated in parallel or on demand (lazily)
; 3. Referential transparency: The value of an expression does not change when we substitute one of its subexpression with the value of that subexpression

; But! No for/while statements!! Can we make basic iteration efficient? Yes!


; ### PYTHON #########################################################
; def factorial(n, k)   # Time O(N), Space O(N)
;   if n == 0:                               |
;     return k                               |
;   else:                                    | Gap of space using
;   return factorial(n-1, k*n)               |
;                                            |
; def factorial(n, k):  # Time O(N), Space O(1)
;   while > n > 0:
;     n, k = n-1, k*n
;   return k
; ### PYTHON end #####################################################


; Tail calls:
; A procedure call that has not yet returned is active.
; Some procedure calls are tail calls.
; A Scheme interpreter should support an unbounded number of active tail calls using on a constant mount of space

; A tail call is a call expression in a tail context
; > The last body sub-expression in a lambda expression
; > Sub-expressions 2 & 3 in a tail context if expression
; > All non-predicate sub-expression in a tail context cond
; > The last sub-expression in a tail context and or or
; > The last sub-expression in a tail context begin

;; Compute n! * k
(define (factorial n k)
  (if (= n 0) k
    (factorial (- n 1)
               (* k n))))   ; This is a tail call, once this run, you can forget n and k
; This should work as Space O(1) but how?



;; Compute the length of well-formed list s.
(define (length s)
  (if (null? s) 0
    (+ 1 (length (cdr s)))))   ; Not a tail call, still need to add 1 after finished the call on the function

; A call expression is not a tail call if more computation is still required in the calling procedure
; Linear recursive procedures can often be re-written to use tail calls.

;; Compute the length of well-formed list s.
(define (length-tail s)
  (define (length-iter s n)
    (if (null? s) n
      (length-iter (cdr s)
                   (+ 1 n)))) ; make the last call as a function
  (length-iter s 0))  ; start with n = 0

;; Compute the length of well-formed list s.
(define (lengthy s)
  (+ 1 (if (null? s)
           -1
           (lengthy (cdr s)))))




;; Return whether s contains v.
(define (contains s v)
  (if (null? s)
      false
      (if (= v (car s))
          true
          (contains (cdr s) v))))

;; Return whether s has any repeated elements
(define (has-repeat s)
  (if (null? s)
      false
      (if (contains? (cdr s) (car s))
          true
          (has-repeat (cdr s)))))

;; Return the nth Fibonacci number.
(define (fib n)
  (define (fib-iter current k)
    (if (= k n)
        current
        (fib-iter (+ current
                     (fib (- k 1)))
                  (+ k 1))))
  (if (= 1 n) 0 (fib-iter 1 2)))

;; Reduce s using procedure and start value.
(define (reduce procedure s start)
  (if (null? s) start
    (reduce procedure
            (cdr s)
            (procedure start (car s)))))

;; Return a copy of s with elements in reverse order.
(define (reverse s)
  (define (reverse-iter s r)
    (if (null? s) r
      (reverse-iter (cdr s)
                    (cons (car s) r))))
  (reverse-iter s nil))

;; Map procedure over s.
(define (map-rec procedure s)
  (if (null? s) nil
    (cons (procedure (car s))
          (map-rec procedure (cdr s)))))

;; Map procedure over s.
(define (map procedure s)
  (define (map-reverse s m)
    (if (null? s) m
      (map-reverse (cdr s)
                (cons (procedure (car s)) m))))
  (reverse (map-reverse s nil)))

;; Tests

(define (assert-equal v1 v2)
  (if (equal? v1 v2) 'okay (list v2 'does 'not 'equal v1)))

(define square (lambda (x) (* x x)))

(assert-equal 360 (factorial 5 3))
(assert-equal 4 (length '(5 6 7 8)))
(assert-equal 4 (length-tail '(5 6 7 8)))
(assert-equal 4 (lengthy '(5 6 7 8)))
(assert-equal #t (contains '(4 5 6) 5))
(assert-equal #f (contains '(4 6 8) 5))
(assert-equal 5 (fib 6))
(assert-equal 1680 (reduce * '(5 6 7 8) 1))
(assert-equal '(5 4 3 2)
              (reduce (lambda (x y) (cons y x)) '(3 4 5) '(2)))
(assert-equal '(8 7 6 5) (reverse '(5 6 7 8)))
(assert-equal '(25 36 49 64) (map-rec square '(5 6 7 8)))
(assert-equal '(25 36 49 64) (map square '(5 6 7 8)))

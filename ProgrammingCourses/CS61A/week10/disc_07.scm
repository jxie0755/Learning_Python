; CS61A Disc 07 Scheme


; Write a function that returns the factorial of a number.

(define (factorial x)
  (if (< x 2)
    1
    (* x (factorial (- x 1)))))


; Write a function that returns the nth Fibonacci number.

(define (fib n)
  (if (< n 2)
    1
    (+ (fib (- n 1)) (fib (- n 2)))))


; Write a function which takes two lists and concatenates them.

(define (concat a b)
  (if (null? a)
    b
    (cons (car a) (concat (cdr a) b))))


; Write a function that takes an element x and a non-negative integer n, and returns
a list with x repeated n times.

(define (replicate x n)
  (if (= n 0)
    nil
    (cons x (replicate x (- n 1)))))


; A run-length encoding is a method of compressing a sequence of letters.

(if (null? s)
  s
  (concat (replicate (car (car s)) (car (cdr (car s))))
    (uncompress (cdr s)))))


; Write a function that takes a procedure and applies it to every element in a given
list.

(define (map fn lst)
  (if (null? lst)
    nil
    (cons (fn (car lst)) (map fn (cdr lst)))))


; Write a function that takes a procedure and applies to every element in a given
nested list.

(define (deep-map fn lst)
  (cond ((null? lst) lst)
    ((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
    (else (cons (fn (car lst)) (deep-map fn (cdr lst))))
  )
)


; Scheme Tree
; Fill in the following to complete an abstract tree data type:

(define (make-tree label branches) (cons label branches))
(define (label tree) (car tree))
(define (branches tree) (cdr tree))

; Using the abstract data type above, write a function that sums up the entries of a
tree, assuming that the entries are all numbers.

(define (tree-sum tree)
  (+ (label tree) (sum (map tree-sum (branches tree)))))

(define (sum lst)
  (if (null? lst) 0 (+ (car lst) (sum (cdr lst)))))

; Using the abstract data type above, write a function that creates a new tree where
the entries are the product of the entries along the path to the root in the original
tree

(define (path-product-tree t)
  (define (path-product t product)
    (let ((prod (* product (label t))))
      (make-tree prod
        (map (lambda (t) (path-product t prod))
          (branches tree)))))
  (path-product t 1))

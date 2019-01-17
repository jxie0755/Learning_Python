; CS61A Disc 08


; Part 1 Calculator

> (+ 1 2 (- 3 4))
>>> Pair('+', Pair(1, Pair(2, Pair(Pair('-', Pair(3, Pair(4, nil))), nil))))

> (+ 1 (* 2 3) 4)
>>> Pair('+', Pair(1, Pair(Pair( '*', Pair(2, Pair(3, nil))), Pair(4,nil))))

>>> Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
(+ 1 2 3 4)

>>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
(+ 1 (* 2 3))


; Part 2 Evaluation

> (+ 2 4 6 8)
; 6 calls to eval: 1 for the entire expression, and then 1 for each operator and operand.
; 1 call to apply the addition operator.

> (+ 2 (* 4 (- 6 8)))
; 10 calls to eval: 1 for the whole expression, then 1 for each of the operators and operands.
; When we encounter another call expression, we have to evaluate the operators and operands inside as well.
; 3 calls to apply each of the operators.

; Q: Alyssa P. Hacker and Ben Bitdiddle are also tasked with implementing the and operator, as in (and (= 1 2) (< 3 4)). Ben says this is easy: they just have to follow the same process as in implementing * and /. Alyssa is not so sure. Who's right?
; A: Alyssa. We can't handle and in the apply step since and is a special form: it is short-circuited. We need to create a special case for it in calc eval.


def calc_eval(exp):
  if isinstance(exp, Pair):
    if exp.first == 'and':
      return eval_and(exp.second)
    else:
      return calc_apply(calc_eval(exp.first), list(exp.second.map(calc_eval)))
  elif exp in OPERATORS:
    return OPERATORS[exp]
  else: # Atomic expression
    return exp

def eval_and(operands):
  curr = operands
  last = True
  while curr is not nil:
    last = calc_eval(curr.first)
    if last is False:
      return False
    curr = curr.second
  return last


; Part 3 Tail-Call Optimaztion
(define (fact n)
  (if (= n 0)
    1
    (* n (fact (- n 1)))))  ; Not a tail call

(define (fact n)
  (define (fact-tail n result)
    (if (= n 0)
      result
      (fact-tail (- n 1) (* n result))))
  (fact-tail n 1))


; Identify below:
(define (question-a x)
  (if (= x 0)
  0
  (+ x (question-a (- x 1))))  ; Not a tail call as x needs to be added after next call


(define (question-b x y)
  (if (= x 0)
     y
     (question-b (- x 1) (+ y x))))  ; Tail call, never end

(define (question-c x y)
  (if (> x y)
    (question-c (- y 1) x)
    (question-c (+ x 10) y)))  ; Tail call, two condition, but only one will be executed every call

(define (question-d n)
  (if (question-d n)
    (question-d (- n 1))
    (question-d (+ n 10))))  ; Not a Tail call, because if call is a recursive. This will never end?


; Tail call version of Fibonacci
(define (fib n)
  (define (fib-sofar i curr next)
    (if (= i n)
      curr
      (fib-sofar (+ i 1) next (+ curr next)))
  (fib-sofar 0 0 1))


; Tail call version of sum
(define (sum lst)
  (define (sum-reduce lst start)
    (if (null? lst)
        start
        (sum-reduce (cdr lst) (+ start (car lst)))))
  (sum-reduce lst 0)


; Write a tail recursive function that takes in a number and a sorted list.
; The function returns a sorted copy with the number inserted in the correct position.
; 3 sub function

; 1 - revser a list
(define (reverse lst)
  (define (reverse_r lst lst-sofar)
    (if (null? lst)
      lst-sofar
      (revers_r (cdr lst) (cons (car lst) lst-sofar))))
  (reverse_r lst nil)

; 2 - write a tail recursive function that concatenates two lists together
(define (append a b)
   (define (rev-append-tail a b)
      (if (null? a)
        b
        (rev-append-tail (cdr a) (cons (car a) b))))
   (rev-append-tail (reverse a) b))


; Finally, implement insert. You may use reverse and append.
(define (insert n lst)
  (define (rev-insert lst rev-lst)
    (cond ((null? lst) (cons n rev-lst))
      ((> (car lst) n) (append (reverse lst)
                                (cons n rev-lst)))
      (else (rev-insert (cdr lst)
                        (cons (car lst) rev-lst)))))
  (reverse (rev-insert lst nil)))


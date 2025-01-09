# Mastermind Solver
A simple solver for almost all variants of the Mastermind game (also known as Bulls and Cows).
Made in Python using Z3 SAT solver.

## How to use
1. Download mastermind_solver.py
2. Install Z3
```bash
pip install z3-solver
```
3. Run mastermind_solver.py

## Example game
```python
Welcome to Mastermind Solver!

Please choose options for the game.
How many numbers in guess: 23
How many different possible numbers: 23
Can numbers repeat (yes or no): y
Warning! This game might take a very long time to complete.

Please choose format for guess output from the following:
(a) 01-02-03-04  08-09-10-11
(b) 00-01-02-03  08-09-10-11
(c) 1-2-3-4  8-9-a-b
(d) 0-1-2-3  8-9-a-b
(e) a-b-c-d  h-i-j-k
Input a, b, c, d or e: a

The game starts!
Found a valid guess 1 in 0.0 seconds.
Use guess:
01-01-01-01-01-01-01-01-01-01-01-01-01-01-01-01-01-01-01-01-01-01-01
Input number of bulls: 0
Number of cows: 0

Found a valid guess 2 in 0.0 seconds.
Use guess:
02-02-02-02-02-02-02-02-02-02-02-02-02-02-02-02-02-02-02-02-02-02-02
Input number of bulls: 0
Number of cows: 0

Found a valid guess 3 in 0.1 seconds.
Use guess:
03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03
Input number of bulls: 0
Number of cows: 0

Found a valid guess 4 in 0.1 seconds.
Use guess:
04-04-04-04-04-04-04-04-04-04-04-04-04-04-04-04-04-04-04-04-04-04-04
Input number of bulls: 1
Number of cows: 0

Found a valid guess 5 in 0.1 seconds.
Use guess:
05-04-05-05-05-05-05-05-05-05-05-05-05-05-05-05-05-05-05-05-05-05-05
Input number of bulls: 0
Input number of cows: 2

Found a valid guess 6 in 0.1 seconds.
Use guess:
06-05-06-06-06-06-06-06-06-04-06-06-06-06-06-06-06-06-06-06-06-06-06
Input number of bulls: 2
Input number of cows: 1

Found a valid guess 7 in 0.2 seconds.
Use guess:
07-05-07-07-07-07-07-07-07-07-07-07-07-07-07-06-07-07-07-07-07-07-04
Input number of bulls: 2
Input number of cows: 2

Found a valid guess 8 in 0.2 seconds.
Use guess:
08-05-08-08-08-08-08-08-06-08-08-08-08-08-08-07-08-08-08-08-08-08-04
Input number of bulls: 4
Input number of cows: 4

Found a valid guess 9 in 0.2 seconds.
Use guess:
08-05-09-09-09-06-09-09-04-07-09-08-09-09-08-08-09-09-09-09-09-09-09
Input number of bulls: 2
Input number of cows: 7

Found a valid guess 10 in 0.3 seconds.
Use guess:
07-05-10-10-10-10-08-04-09-10-10-10-10-10-08-10-10-10-06-10-10-08-08
Input number of bulls: 4
Input number of cows: 8

Found a valid guess 11 in 0.4 seconds.
Use guess:
08-05-11-11-11-08-11-11-08-09-11-04-10-11-11-10-11-10-11-08-11-07-06
Input number of bulls: 4
Input number of cows: 9

Found a valid guess 12 in 0.4 seconds.
Use guess:
07-05-12-12-12-12-10-04-12-09-10-12-08-11-12-08-08-12-12-12-08-10-06
Input number of bulls: 1
Input number of cows: 13

Found a valid guess 13 in 0.4 seconds.
Use guess:
10-05-07-13-06-08-11-10-09-13-13-04-12-08-08-13-13-13-10-13-13-13-08
Input number of bulls: 2
Input number of cows: 13

Found a valid guess 14 in 0.6 seconds.
Use guess:
09-05-08-14-14-11-13-07-08-14-14-10-10-14-08-14-14-14-04-08-06-12-10
Input number of bulls: 7
Input number of cows: 10

Found a valid guess 15 in 0.7 seconds.
Use guess:
09-05-11-08-15-15-12-15-04-10-15-10-15-13-10-14-14-15-08-08-06-07-08
Input number of bulls: 4
Input number of cows: 13

Found a valid guess 16 in 1.1 seconds.
Use guess:
13-05-08-16-08-09-12-11-08-10-16-16-14-16-08-10-07-16-04-14-06-16-10
Input number of bulls: 4
Input number of cows: 13

Found a valid guess 17 in 2.2 seconds.
Use guess:
08-05-17-14-14-11-13-12-10-17-17-17-10-17-09-10-07-08-08-04-06-17-08
Input number of bulls: 5
Input number of cows: 13

Found a valid guess 18 in 1.3 seconds.
Use guess:
18-05-08-18-14-08-07-12-08-14-17-10-18-13-10-18-11-09-06-04-18-08-10
Input number of bulls: 6
Input number of cows: 13

Found a valid guess 19 in 1.8 seconds.
Use guess:
09-05-18-14-08-06-08-12-08-17-14-10-19-08-13-19-10-19-11-04-19-07-10
Input number of bulls: 5
Input number of cows: 14

Found a valid guess 20 in 2.8 seconds.
Use guess:
13-05-20-14-08-06-07-20-10-14-08-10-10-12-20-09-11-17-04-08-18-20-08
Input number of bulls: 3
Input number of cows: 16

Found a valid guess 21 in 2.4 seconds.
Use guess:
08-05-08-18-21-09-21-07-13-08-14-10-21-21-10-10-06-14-11-04-17-12-08
Input number of bulls: 6
Input number of cows: 14

Found a valid guess 22 in 3.4 seconds.
Use guess:
09-05-08-07-21-22-13-10-08-10-12-08-10-17-22-14-06-22-11-04-18-08-14
Input number of bulls: 3
Input number of cows: 18

Found a valid guess 23 in 2.4 seconds.
Use guess:
22-05-08-14-10-08-21-18-08-17-23-10-09-13-06-04-07-14-08-10-11-12-23
Input number of bulls: 6
Number of cows: 17

Found a valid guess 24 in 6.1 seconds.
Use guess:
23-05-18-08-14-21-17-11-08-08-14-10-10-22-10-04-07-08-06-23-13-12-09
Input number of bulls: 7
Number of cows: 16

Found a valid guess 25 in 17 seconds.
Use guess:
22-05-04-18-14-09-08-17-08-07-14-23-10-08-10-23-11-21-08-10-06-12-13
Input number of bulls: 8
Number of cows: 15

Found a valid guess 26 in 23 seconds.
Use guess:
08-05-17-18-14-22-08-11-08-23-04-10-21-06-23-09-14-07-08-10-13-12-10
Input number of bulls: 6
Number of cows: 17

Found a valid guess 27 in 18 seconds.
Use guess:
23-05-09-22-14-08-17-07-08-11-08-10-14-21-18-23-10-10-08-04-06-12-13
Input number of bulls: 11
Number of cows: 12

Found a valid guess 28 in 37 seconds.
Use guess:
17-05-10-10-22-08-18-11-08-14-14-10-23-21-07-23-09-08-08-04-06-12-13
Input number of bulls: 9
Number of cows: 14

Found a valid guess 29 in 36 seconds.
Use guess:
13-05-23-21-14-08-09-17-08-08-14-10-07-10-18-22-23-10-08-04-06-12-11
Input number of bulls: 19
Number of cows: 4

Found a valid guess 30 in 7.4 seconds.
Use guess:
13-05-23-23-14-08-09-17-08-08-14-10-07-10-18-11-21-10-08-04-06-12-22
Input number of bulls: 20
Number of cows: 3

Found a valid guess 31 in 2.2 seconds.
Use guess:
13-05-22-23-14-08-09-17-08-08-14-10-07-10-18-11-23-10-08-04-06-12-21
Input number of bulls: 23
Number of cows: 0

Congratulations, game won!
Total guesses: 31. Processing time: 2 minutes and 48 seconds.
```

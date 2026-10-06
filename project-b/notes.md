I DIDN'T REALIZE THERE WAS SUPPOSED TO BE A
SEPARATE TOTAL.PY. Since they are so similar,
I've included 15 runs of total.py instead. 
The same information is visible.

RUNS:

1.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 6
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 4
+ ANSWER 21, 7
# yeah that's right.
Tokens used: 471

2.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 6
+ ANSWER 24, 7 rolls
# yeah that's right.
Tokens used: 668

3.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
... didn't complete

4.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 6
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 6
+ ANSWER 22, 6 rolls
# yeah that's right.
Tokens used: 631

5.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 6
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 6
+ ANSWER 26, 6
# yeah that's right.
Tokens used: 541

What Gemma did differently:
- Put the system prompt in an external file. I would rather maintain this version if the system prompt gets quite long.
- The model assumed an output format that might not always be accurate. While mine isn't perfect, it does handel more cases. I would rather maintain mine, although I would redesign it to be cleaner if it needed to be expanded.

10 more runs:

1.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 4
+ ANSWER 21, 7
# yeah that's right.
Tokens used: 472

2.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
... didn't complete

3.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 6
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 3
+ ANSWER 21, 6 rolls
# yeah that's right.
Tokens used: 414

4.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 3
+ ANSWER 21, 6
# yeah that's right.
Tokens used: 655

5.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 3
+ ANSWER 23, 7
# yeah that's right.
Tokens used: 660

6.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 6
+ ANSWER 25, 8
# yeah that's right.
Tokens used: 475

7.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 5
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 6
+ CALL roll_die
- roll_die returned 6
+ ANSWER 26, 6
# yeah that's right.
Tokens used: 836

8.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 6
+ ANSWER 21, 6
# yeah that's right.
Tokens used: 670

9.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 3
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 5
+ ANSWER 23, 8
# yeah that's right.
Tokens used: 563

10.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 6
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 4
+ CALL roll_die
- roll_die returned 6
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 4
+ ANSWER 24, 6
# yeah that's right.
Tokens used: 429

A couple rigged runs:

1.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 1
Out of turns. Used 506 tokens.

2.
Roll a die until the running total is more than 20. Tell me first the total and then how many rolls it took.
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 2
+ CALL roll_die
- roll_die returned 1
+ CALL roll_die
- roll_die returned 2
Out of turns. Used 492 tokens.

When was the model wrong?
It didn't get any numbers wrong a single time.
The model we're using is able to add numbers reliably.
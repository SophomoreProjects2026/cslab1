## Our team's spec. Not the one we implemented.

Write a program that splits an arbitrary bill between N people in Python. Accept user input for the bill amount (which should be a floa) and the number of people to split it between. The number of people must be at least 1, and must be an integer. Prompt the user to try again upon entering an invalid input. Output the amount per-person as a dollar amount with no more than two cents precision. Round up to the nearest cent.

## Their team's spec that we implemented:

Take one positive float with two or fewer decimal places (D) and one positive integer (N). Divide D by N (not integer division) and round DOWN to nearest hundredth. Create a list of N copies of that number. Calculate leftover cents by multiplying rounded result by N and subtracting that from D. This should be an integer, let's call it L. Loop through the first L elements in out list and add 0.01 to each of these elements. Print all elements in the list separated by commas. 
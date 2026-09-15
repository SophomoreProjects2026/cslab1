# written by agent
def solve(D, N):
    # Convert D to cents to avoid floating point precision issues
    D_cents = int(round(D * 100))
    
    # Divide D by N and round down to the nearest hundredth
    # Using integer math: floor(D_cents / N)
    res_cents = D_cents // N
    
    # Create a list of N copies of the rounded result
    res_list_cents = [res_cents] * N
    
    # Calculate leftover cents L
    # L = (D - (rounded_result * N)) * 100
    L = D_cents - (res_cents * N)
    
    # Loop through the first L elements and add 0.01 (1 cent) to each
    for i in range(L):
        res_list_cents[i] += 1
        
    # Print all elements in the list separated by commas, formatted to two decimal places
    print(", ".join(f"{x/100:.2f}" for x in res_list_cents))

# written by group
# solve(100, 4) # works
# solve(100.01, 4) # works; distributes remaining cent
# solve(.02, 5) # works; distributes cents
# solve(100.015, 4) # works; rounds to nearest cent
# solve(100.01, -4) # fails; no output
# solve(100, 3.5) # fails; error
# solve(100.01, 0) # fails; error
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
join_A_and_B = A.union(B)

# Find A intersection B
intersection_A_and_B = A.intersection(B)

# Is A subset of B
is_A_subset_of_B = A.issubset(B)

# Are A and B disjoint sets
are_A_and_B_disjoint = A.isdisjoint(B)

# Join A with B and B with A
join_A_and_B = A.union(B)
join_B_and_A = B.union(A)

# What is the symmetric difference between A and B
symmetric_difference_A_and_B = A.symmetric_difference(B)

# Delete the sets completely
del A
del B
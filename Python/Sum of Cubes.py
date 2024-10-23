def sum_of_cubes(M, N):
    if M > N:
        return 0
    return sum(i**3 for i in range(M, N + 1))

M = int(input("Enter M: "))
N = int(input("Enter N: "))

result = sum_of_cubes(M, N)
if result == 0:
    print("M is greater than N, returning 0.")
else:
    print(f"Sum of cubes from {M} to {N} is {result}")

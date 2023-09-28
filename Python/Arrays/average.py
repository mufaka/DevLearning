# python3 average.py
scores = [ 72, 73, 33 ]; 
print(f"Array length: {len(scores)}")

total = 0

for score in scores:
    total += score
    print(f"Total: {total}, {score}")

print(f"Total: {total}")
print(f"Average: {total / len(scores)}")
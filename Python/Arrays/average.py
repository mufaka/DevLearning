# python3 average.py


def array_average(scores):
    total = 0

    for score in scores:
        total += score
        print(f"Total: {total}, {score}")

    print(f"Total: {total}")
    return total / len(scores)


scores = [72, 73, 33]
print(f"Array length: {len(scores)}")

average = array_average(scores)

print(f"Average: {average}")

""" In the below example, we’ve chained two functions, the first finds the prime number between 1 to 100, and the latter selects the odd one from them. """

def find_prime():
    num = 1
    while num < 100:
        if num > 1:
            for i in range(1, num):
                if (num % i ) == 0:
                    break
                else:
                    yield num
            num += 1
def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num
a_pipeline = find_odd_prime(find_prime())
for a_ele in a_pipeline:
    print(a_ele)


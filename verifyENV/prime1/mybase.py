import math
import itertools

def gen_primes_upto(n):
    """Generates a sequence of primes < n.

    Uses the full sieve of Eratosthenes with O(n) memory.
    """
    if n == 2:
        return

    table = [True] * n
    sqrtn = int(math.ceil(math.sqrt(n)))

    for i in range(2, sqrtn):
        if table[i]:
            for j in range(i * i, n, i):
                table[j] = False

    yield 2
    for i in range(3, n, 2):
        if table[i]:
            yield i

def gen_primes_upto_segmented(n):
    """Generates a sequence of primes < n.

    Uses the segmented sieve or Eratosthenes algorithm with O(√n) memory.
    """
    # Simplify boundary cases by hard-coding some small primes.
    if n < 11:
        for p in [2, 3, 5, 7]:
            if p < n:
                yield p
        return

    # We break the range [0..n) into segments of size √n
    segsize = int(math.ceil(math.sqrt(n)))

    # Find the primes in the first segment by calling the basic sieve on that
    # segment (its memory usage will be O(√n)). We'll use these primes to
    # sieve all subsequent segments.
    baseprimes = list(gen_primes_upto(segsize))
    for bp in baseprimes:
        yield bp

    for segstart in range(segsize, n, segsize):
        # Create a new table of size √n for each segment; the old table
        # is thrown away, so the total memory use here is √n
        # seg[i] represents the number segstart+i
        seg = [True] * segsize

        for bp in baseprimes:
            # The first multiple of bp in this segment can be calculated using
            # modulo.
            first_multiple = (
                segstart if segstart % bp == 0 else segstart + bp - segstart % bp
            )
            # Mark all multiples of bp in the segment as composite.
            for q in range(first_multiple, segstart + segsize, bp):
                seg[q % len(seg)] = False

        # Sieving is done; yield all composites in the segment (iterating only
        # over the odd ones).
        start = 1 if segstart % 2 == 0 else 0
        for i in range(start, len(seg), 2):
            if seg[i]:
                if segstart + i >= n:
                    break
                yield segstart + i

D = []
N = 100
for x in gen_primes_upto_segmented(N):
    D.append(x)
print(D)

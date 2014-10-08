import uuid
from hll import HLL

if __name__ == '__main__':
    h = HLL()
    n = 10000
    for i in xrange(n):
        u = str(uuid.uuid4())
        # Add twice to make sure it only gets counted once.
        h.add(u)
        h.add(u)

    print 'Actual: {}, Estimated: {}'.format(n, h.count())

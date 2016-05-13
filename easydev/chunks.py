



'''http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python

Here's a generator that yields the chunks you want:

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

The issue here is that the chunks are not evenly sized chunks

'''


#Here's a balanced solution, adapted from a function I've used in production
#(Note in Python 3 to replace xrange with range):

try:
    range = xrange # py2
except:
    pass  #py3


def baskets_from(items, maxbaskets=25):
    baskets = [[] for _ in range(maxbaskets)] 
    for i, item in enumerate(items):
        baskets[i % maxbaskets].append(item)
    return filter(None, baskets) 

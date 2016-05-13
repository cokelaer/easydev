



'''http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python

Here's a generator that yields the chunks you want:

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

The issue here is that the chunks are not evenly sized chunks

'''


__all__ = ['split_into_chunks']


try:
    range = xrange # py2
except:
    pass  #py3


def split_into_chunks(items, maxchunks=10):
    """Split a list evenly into N chunks"""
    chunks = [[] for _ in range(maxchunks)] 
    for i, item in enumerate(items):
        chunks[i % maxchunks].append(item)
    return filter(None, chunks) 

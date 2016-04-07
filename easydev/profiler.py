"""

Usage::

    from easydev import profiler
    @do_profile()
    def test():
        x = 1
        x *= x
        return x

# source: https://zapier.com/engineering/profiling-python-boss/


Requires line_profiler to be installed. line_profiler has C code and we wish
easydev to be as simple as possible. So, we do not want compiled code dependencies.
Consequently, we added line_profiler in the extra_requires instead of requires
in the setup.py One must install line_profiler itself.
"""

__all__ = ["do_profile"]

try:
    from line_profiler import LineProfiler
    def do_profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner
except ImportError:
    def do_profile(follow=[]):
        "Helpful if you accidentally leave in production!"
        print("easydev warning:: line_profiler does not seem to be installed. " + 
            "Type 'pip install line_profiler'")
        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return inner


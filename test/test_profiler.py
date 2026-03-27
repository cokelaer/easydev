from easydev import do_profile


def test_do_profile_wraps_and_runs():
    results = []

    @do_profile()
    def compute():
        results.append(42)
        return 42

    ret = compute()
    assert ret == 42
    assert results == [42]


def test_do_profile_with_follow():
    def helper():
        return 1

    @do_profile(follow=[helper])
    def compute():
        return helper() + 1

    assert compute() == 2


def test_do_profile_preserves_args():
    @do_profile()
    def add(a, b):
        return a + b

    assert add(3, 4) == 7

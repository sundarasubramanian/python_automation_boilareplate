import random


def test_flaky_example():
    """A deliberately flaky test to demonstrate rerun behaviour.

    This test randomly fails ~50% of the time. With pytest-rerunfailures enabled
    (default --reruns=2) the test will be retried up to 2 times before final failure.
    """
    assert random.choice([True, False]), 'Flaky failure: random choice was False'

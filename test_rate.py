"""Module for testing the Rate object"""
import time

from tftime import Rate


def test_rate():

    freq = 2
    r = Rate(freq=freq)
    start_time = time.perf_counter()
    r.sleep()
    total_time = time.perf_counter() - start_time
    print(f"Took {total_time}s")
    assert total_time - 1.0 / freq < 0.01

    iterations = 10
    count = iterations
    start_time = time.perf_counter()
    while count > 0:
        print(count)
        count -= 1
        r.sleep()

    total_time = time.perf_counter() - start_time
    print(f"Took {total_time}s for {iterations} iterations")
    assert total_time - iterations / freq < 0.001

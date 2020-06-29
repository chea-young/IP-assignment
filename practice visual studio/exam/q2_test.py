def queue_time(customers, n):
    pass

def test_q2():
    assert queue_time([], 1)== 0
    assert queue_time([5], 1) == 5
    assert queue_time([2], 5) == 2
    assert queue_time([1,2,3,4,5], 1) == 15
    assert queue_time([1,2,3,4,5], 100) == 5
    assert queue_time([2,2,3,3,4,4], 2) == 9

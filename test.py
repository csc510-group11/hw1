from myfile import pow

def test_success():
    assert(pow(2, 3) == 8)

def test_failure():
    assert(pow(3, 0) == 3)
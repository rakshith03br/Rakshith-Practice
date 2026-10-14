import pytest

@pytest.fixture(params=[1,2,3,4])
def par_fix(request):
    print(request.param)

def test_add(par_fix):
    print("Added successfully")


par = [('a'),('b'),('c'),('d'),]
@pytest.mark.parametrize("process",par)
def test_sum(process):
    print(process)
    
import pytest

class Test:

    @pytest.mark.parametrize(["a", "b"], [(1, 2), (3, 4)])
    def test_t_pos(self, a, b, fun_setup):
        assert a + 1 == b


    @pytest.mark.parametrize("a,b,c",[(1,2,3),(2,4,6)])
    def test_add(self, a,b,c, cl_setup):
        assert a+b == c

#################################################
def get_id_list():
    return ['a1', 'a2', 'a3']


@pytest.mark.parametrize("process", get_id_list())
def test_my_function(process):
    print(process)
    assert process



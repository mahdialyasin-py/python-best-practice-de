from simple_pytest_sk.arithmetic import sign, lerp


def test_sign_for_positive_number():
    assert sign(2) == 1

def test_sign_for_negative_number():
    assert sign(-20) == -1

def test_sign_for_zero():
    assert sign(0) == 0

class TestLerp: 
     # Klasse muss mit Test anfangen
    def test_for_t_eq_0(self):
        assert lerp(1, 3, 0) == 1

    def test_for_t_eq_1(self):
        assert lerp(1, 3, 1) == 3

    def test_for_intermediate_t(self):
        assert lerp(1, 3, 0.5) == 2.0

    def somthing_else(self):
        print("hallo")

    
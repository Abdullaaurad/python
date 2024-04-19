import Math

def test_add():
    assert Math.Add(5,6)==11
    assert Math.product(2,3)==6
    assert Math.Add(2,2)==3   #Wrong
    assert Math.product(5,5)==26  #Wrong

test_add()
# pytest test_Math.py
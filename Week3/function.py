def deposit_amt(amt):
    print("start")
    assert amt> 0
    print('finished')

# deposit_amt(-2)

# def test__min():
#     assert min(1,3,5,5) < 2
#     print('done')
# test__min()
#

# def test__check():
#     assert 7.135 == 7.128
#     print('CHECK')
# test__check()

e = 7.135
f =  7.128
if abs(f-e) < 0.01:
    print('this')
else:
    print('that')
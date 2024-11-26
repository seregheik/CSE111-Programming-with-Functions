from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Osasere','Ikponmwosa') == 'Ikponmwosa;Osasere'

def test_extract_family_name():
    assert extract_family_name('Ikponmwosa;Osasere') == 'Ikponmwosa'
def test_extract_given_name():
    assert extract_given_name('Ikponmwosa;Osasere') == 'Osasere'


pytest.main(['-v', '--tb=liine', '-rN', __file__])
import pytest
import hypothesis.strategies as st
from hypothesis import given
import pytest

def testing_fun1():
    assert pytest.dict([1, 2, '3'], ['Py', '0', 'None']) == {1: 'Py', 2: '0', '3': 'None'},'1'

@given(st.sets(st.integers()), st.sets(st.integers()))
def test(keys, values):
    keys = list(keys)
    values = list(values)
    dictionary =  pytest.dict(keys, values)

    if len(keys) < len(values):
        values = values[0:len(keys):]
    if len(values) < len(keys):
        for i in range(len(keys) - len(values)):
            values.append(None)

    assert list(dictionary.keys()) == keys
    assert list(dictionary.values()) == values
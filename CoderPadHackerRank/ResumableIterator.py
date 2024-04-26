"""

A typical iterator supports a single method, `next()`, which returns the next element.  For example, in python:

```python
it = iter([1,2,3])
assert it.__next__() == 1
assert it.__next__() == 2
assert it.__next__() == 3
with pytest.raises(StopIteration):
    it.__next__()
```

However, this gives no way to go backwards to previous states of the iterator.  Thus we would like a "resumable iterator" which additionally supports getting and setting state.  (This is useful in ML training for saving state of dataset iteration, for example.)

```python
it = resumable_iter([1,2,3])
assert it.__next__() == 1
s = it.get_state()
assert it.__next__() == 2
assert it.__next__() == 3
it.set_state(s)  # go back to previous point of iteration!
assert it.__next__() == 2
assert it.__next__() == 3
```

The important guarantee is that set_state(..) with a prior result of get_state() restores to the previous point in time, replicating that behavior.  Essentially, we can move forward in the stream, and we can also move backwards in the stream, but only if we saved the state.

Your task is to:

- In your language of choice, write an interface or abstract class for resumable iterators with operations `next()`, `get_state()`, `set_state(s)`.  You do *not* need to implement the interface.
- Write a test function, e.g. `def test_resumable_iterator(it, expected_elements): ...` for your new interface exercising the functionality.  It should test that iteration works as expected, and that resumption works at every state.  The test should pass for *any* implementation of the interface, with only the assumption that there are only finitely many elements!
   
"""
class ResumableIterator:
    def __init__(self) -> None:
        self.data = []



# I : [1, 4, 2, 3]

# I: [1, 2, 3]
# indexList: [1, 2, 3]
def test_resumable_iteratorV1(it, expected_elements):
    stateIndex = 0 # handle get and set logic
    next = 0 # next iterator pointer to elemnet will pop when call it.__next__()
    indexList = [0] # initial value from index zero
    stateList = [it.get_state()] # initial value to 1st state
    for i, element in enumerate(expected_elements): # 0
        assert it.__next__() == element
        s = it.get_state()
        stateList.append(s)
        stateIndex = i + 1 # 1
        indexList.append(stateIndex)
        # collect state in list

    # print(f"indexList: {indexList}")
    # print(f"stateList: {stateList}")
    
    # for each of our saved states:
    # 1. resume at that state 
    # 2. do a pass from that state and ensure that we get the right values + behavior
    for i, s in enumerate(stateList): # [0, 1, 2, 3]
        it.set_state(s) # state map to next value is 1
        stateIndex = indexList[i] # 0, 1
        for j in range(stateIndex, len(indexList) - 1): #0
            # print("j", j)
            element = expected_elements[j] #1
            assert it.__next__() == element


def test_resumable_iteratorV0(it, expected_elements):
    for element in expected_elements:
        assert it.__next__() == element

    left = 0 # handle get and set logic
    next = 0 # next iterator pointer to elemnet will pop when call it.__next__()
    for i, element in enumerate(expected_elements):
        assert it.__next__() == expected_elements[next]
        next += 1
        left = next

        if i == 1:
            s = it.get_state()
            left = i

        if i == 4:
            it.set_state(s)
            next = left
        


    # assert it.__next__() == 1
    # s = it.get_state()
    # assert it.__next__() == 2
    # assert it.__next__() == 3
    # it.set_state(s)  # go back to previous point of iteration!
    # assert it.__next__() == 2
    # assert it.__next__() == 3


# expected_elements = [1,2,3]

    # expected_elements = [("next", 1),("get", 1),("next", 2),("next", 3),("set", 1),("next", 2),("next", 3)]
    # expected_operations = [("next", 1),("get", 1),("next", 2),("next", 3),("set", 1),("next", 2),("next", 3)]

# it = resumable_iter([1,2,3])
# test_resumable_iterator(it, expected_elements)


"""

Now implement your resumable iterator interface for the case of a simple in-memory list, and make sure your tests pass.

In Python, this should look something like

```python

```
and we should be able to run

```
my_list = [1, 4, 2, 3]
test_resumable_iterator(ListIterator(my_list), my_list)
```

"""

class ListIterator(ResumableIterator):
    def __init__(self, lst):
        self.data = lst.copy()
        self.next = 0
        self.stateIndex = 0

    def __next__(self): #1
        if self.next < len(self.data):
            res = self.data[self.next]
            self.next += 1 # 2
            return res
        else:
            print("out of bound")

    def get_state(self):
        self.stateIndex = self.next
        return self.stateIndex

    def set_state(self, s):
        self.next = s
        return 

my_list = [1, 4, 2, 3]
test_resumable_iteratorV1(ListIterator(my_list), my_list)


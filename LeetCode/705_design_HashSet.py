class MyHashSet:
    """
    https://www.youtube.com/watch?v=VymjPQUXjL8
    
    beats 15.84%
    """
    def __init__(self):
        self.hashset = []        

    def add(self, key: int) -> None:
        if not (key in self.hashset):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return (key in self.hashset)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

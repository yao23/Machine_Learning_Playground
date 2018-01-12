class Cell:
    """
    Implement Cell class to indicate element key and value
    """
    key = 0
    val = 0

    def __init__(self, key, val):
        """
        :param key:
        :param val:

        Initialize node cell
        """
        self.key = key
        self.val = val

    def get_key(self):
        """
        :return:

        Get key
        """
        return self.key

    def get_value(self):
        """
        :return:

        Get value
        """
        return self.val


class HashTable:
    """
    Implement Hash Table with an array with constant size
    Hash Function is length of key mod by array size
    If collided, use chaining technique to append to the node list
    """

    def __init__(self):
        """
        Initialize Hash Table
        """
        self.max_len = 10
        self.hash_table_arr = []

    def hash_of_key(self, element_key):
        """
        :param element_key:
        :return:

        Get hash of key
        """
        return len(element_key) % self.max_len

    def get_element(self, element_key):
        """
        :param element_key:
        :return:

        Get element in Hash Table
        """
        node_list = self.hash_table_arr[self.hash_of_key(element_key)]
        if node_list:
            for i, node in enumerate(node_list):
                if node.key == element_key:
                    return node.get_value()
            return -1
        else:
            return -1

    def put_element(self, element_key, element_value):
        """
        :param element_key:
        :param element_value:
        :return:

        Put element in Hash Table
        """
        node_list = self.hash_table_arr[self.hash_of_key(element_key)]
        if node_list:
            for i, node in enumerate(node_list):
                if node.key == element_key:
                    node.value = element_value
            node_list.append(Cell(element_key, element_value))
        else:
            node_list.append(Cell(element_key, element_value))

    def debug_print_hash(self):
        for i in range(len(self.hash_table_arr)):
            print("%d : " % i)
            item_list = self.hash_table_arr[i]
            if item_list:
                for cell in item_list:
                    print(cell.to_string() + ", ")

            print("")


class Dummy:
    """
    Test Dummy Class
    """
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def to_string(self):
        return "(" + self.__name + ", " + self.__age + ")"

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


class TestSolution:
    """
    Test Solution Class
    """
    def __init__(self):
        bob = Dummy("Bob", 20)
        jim = Dummy("Jim", 25)
        alex = Dummy("Alex", 30)
        tim = Dummy("Tim", 35)
        maxwell = Dummy("Maxwell", 40)
        john = Dummy("John", 45)
        julie = Dummy("Julie", 50)
        christy = Dummy("Christy", 55)
        tim2 = Dummy("Tim2", 100)  # this should replace the first Tim
        dummies = [bob, jim, alex, tim, maxwell, john, julie, christy, tim2]

        hash_instance = HashTable()
        for index, dummy in enumerate(dummies):
            hash_instance.put_element(dummy.get_name(), dummy)

        hash_instance.debug_print_hash()

        # Test: Recall
        for index, dummy in enumerate(dummies):
            name = dummy.get_name()
            dummy = hash_instance.get_element(name)
            print("Dummy named %s : %s" % (name, dummy.to_string()))

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
    max_len = 10
    hash_table_arr = []

    def __init__(self):
        """
        Initialize Hash Table
        """
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

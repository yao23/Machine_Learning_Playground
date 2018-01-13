import datetime


class Entry:
    """
    Entry
    """
    def __init__(self, name, parent):
        self._name = name
        self._parent = parent
        self._created_time = datetime.date
        self._last_updated_time = 0
        self._last_accessed_time = 0
        self._size = 0

    def delete_entry(self, entry=None):
        if self._parent:
            return self._parent.delete_entry(self)
        else:  # not exist
            return False

    def get_size(self):
        return self._size

    def get_full_path(self):
        if self._parent:
            return self._parent.get_full_path() + "/" + self._name
        else:
            return self._name

    def get_creation_time(self):
        return self._created_time

    def get_last_updated_time(self):
        return self._last_updated_time

    def get_last_accessed_time(self):
        return self._last_accessed_time

    def change_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class File(Entry):
    """
    File
    """
    def __init__(self, name, parent, size, content=""):
        super(File, self).__init__(name, parent)
        self._size = size
        self._content = content

    def get_size(self):
        return self._size

    def get_content(self):
        return self._content

    def set_content(self, content):
        self._content = content


class Directory(Entry):
    """
    Directory
    """
    def __init__(self, name, parent):
        super(Directory, self).__init__(name, parent)
        self._contents = []  # list of entry

    def get_contents(self):
        return self._contents

    def get_size(self):
        size = 0
        for entry in self._contents:
            size += entry.get_size()
        return size

    def get_num_of_files(self):
        count = 0
        for entry in self._contents:
            if isinstance(entry, Directory):
                count += 1  # Directory counts as a file
                directory = Directory(entry, None)
                count += directory.get_num_of_files()
            elif isinstance(entry, File):
                count += 1

        return count

    def delete_entry(self, entry):
        return self._contents.remove(entry)

    def add_entry(self, entry):
        self._contents.append(entry)


class FileSystem:
    """
    File System
    """
    def __init__(self):
        root = Directory("Food", None)
        taco = File("Taco", root, 4)
        hamburger = File("Hamburger", root, 9)
        root.add_entry(taco)
        root.add_entry(hamburger)

        healthy = Directory("Healthy", root)
        fruits = Directory("Fruits", healthy)
        apple = File("Apple", fruits, 5)
        banana = File("Banana", fruits, 6)
        fruits.add_entry(apple)
        fruits.add_entry(banana)

        healthy.add_entry(fruits)
        veggies = Directory("Veggies", healthy)
        carrot = File("Carrot", veggies, 6)
        lettuce = File("Lettuce", veggies, 7)
        peas = File("Peas", veggies, 4)
        veggies.add_entry(carrot)
        veggies.add_entry(lettuce)
        veggies.add_entry(peas)

        healthy.add_entry(veggies)
        root.add_entry(healthy)

        print(root.get_num_of_files())
        print(veggies.get_full_path())

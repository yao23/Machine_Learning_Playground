import constant
import glob
from item import Item
from collation_set import CollationSet
from purchase_history import PurchaseHistory


def load_item_image(item_image_folders):
    """Load item image.

       Args:
           item_image_folders: paths of item image folders.

        Returns:
            a dictionary of {item_id: item image path}
    """
    # TODO: finish the codes here


def load_item_info(item_info_path, item_image_folders):
    """ Item info.

        Args:
           item_info_path: path of item information file.
           item_image_folders: folders of item images.

        Returns:
            {item_id: ITEM(id, cat_id, image_path)}
    """
    # TODO: finish the codes here


def load_collation_set(collation_set_path):
    """ Load collation set.

        Args:
            collation_set_path: path of collation set file.

        Returns:
            a list of collation sets. For example
                [CollationSet([[1,2],[3],[4]]), CollationSet([[1],[9],[5]]), ....]
    """
    collation_set_list = []
    with open(constant.COLLATION_SET_FILE) as input_file:
        for line in input_file:
            line_arr = line.split(' ')
            match_list = line_arr[1]
            match_list_arr = match_list.split(';')
            collation_set = CollationSet(match_list_arr)
            collation_set_list.append(collation_set)
        return collation_set_list

def load_bought_history(bought_history_path):
    """ Load bought history records.

        Args:
            bought_history_path: path of match set file.

        Returns:
            a dictionary of purchased history. For example
            {user_id, BoughtHistory([1,2,3])}
    """
    # TODO: finish the codes here
    purchase_history_dic = []
    with open(bought_history_path) as input_file:
        for line in input_file:
            line_arr = line.split(' ')
            match_list = line_arr[1]
            match_list_arr = match_list.split(';')
            collation_set = CollationSet(match_list_arr)
            purchase_history_dic.append(collation_set)
        return purchase_history_dic


if __name__ == '__main__':
    print 'Bingo'
    # TODO: write some codes to test each function or write independent test class
    # like http://docs.python-guide.org/en/latest/writing/tests/

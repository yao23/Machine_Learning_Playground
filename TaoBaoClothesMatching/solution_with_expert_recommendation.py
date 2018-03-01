class ClotheMatchingSystem:
    """
    class which represents Taobao Clothes Matching System
    """
    def __init__(self):
        """
        init method
        """
        pass

    def is_in_list(self, item_id, clothe_list):
        """
        :param item_id:
        :param clothe_list:
        :return:

        check item id is in clothes list or not
        """
        clothes = clothe_list.split(',')
        for clothe_id in clothes:
            if item_id == int(clothe_id):
                return True
        return False

    def get_match_list(self, item_id):
        """
        :param item_id:
        :return:

        get match list with the given item id
        """
        with open('./data/dim_fashion_matchsets.txt') as input_file:
            for line in input_file:
                tmp_line_arr_1 = line.split(' ')
                match_list = tmp_line_arr_1[1]
                tmp_line_arr_2 = match_list.split(';')
                target_index = -1
                result_list = ''
                for idx, clothes in enumerate(tmp_line_arr_2):
                    if self.is_in_list(item_id, clothes):
                        target_index = idx
                    else:
                        result_list = (result_list + clothes + ';')
                if target_index == -1:
                    return ''
                else:
                    return result_list[:-1]

    def test_items(self):
        """
        :return:

        test method to get matching list with item ids
        """
        with open('./data/test_items.txt') as input_file:
            for line in input_file:
                item_id = int(line)
                match_list = self.get_match_list(item_id)
                if match_list:
                    print("item: %d, get matching list: %s" % (item_id, match_list))


clothes_matching_system = ClotheMatchingSystem()
clothes_matching_system.test_items()  # 1417 is a test example, should return "160870;3118604"

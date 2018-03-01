class ClotheMatchingSystem:
    """
    class which represents Taobao Clothes Matching System
    """
    def __init__(self):
        """
        init method (data path)
        """
        self.test_item_path = './data/test_items.txt'
        self.item_data_path = './data/dim_items.txt'
        self.example_result_path = './data/example_result.txt'
        self.purchase_data_path = './data/user_bought_history.txt'
        self.expert_recommendation_path = './data/dim_fashion_matchsets.txt'
        self.model_on_expert_data = './model/model_on_expert_data.txt'

        self.train_model_with_expert_data()

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
        with open(self.expert_recommendation_path) as input_file:
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

    def get_match_items(self, index, clothes_list):
        """
        :param index:
        :param clothes_list:
        :return:

        get match items based on expert recommendation data
        """
        match_items = ''
        for idx, clothes in enumerate(clothes_list):
            if idx == index:
                continue
            else:
                match_items = match_items + clothes.rstrip('\n') + ";"
        return match_items[:-1]

    def train_model_with_expert_data(self):
        """
        :return:

        train model based on expert recommendation data
        """
        with open(self.expert_recommendation_path) as data_file, \
                open(self.model_on_expert_data, 'a') as model_file:
            # count = 0
            for line in data_file:
                # count += 1
                # if count > 3:
                #     break
                line_arr_1 = line.split(' ')
                match_list = line_arr_1[1]
                line_arr_2 = match_list.split(';')
                for idx, clothes_list in enumerate(line_arr_2):
                    clothes = clothes_list.split(',')
                    for clothe_id in clothes:
                        tmp_result = clothe_id.rstrip('\n') + ' ' + self.get_match_items(idx, line_arr_2)
                        # print(tmp_result)
                        model_file.write(tmp_result + '\n')

    def test_items(self):
        """
        :return:

        test method to get matching list with item ids
        """
        with open(self.test_item_path) as input_file:
            for line in input_file:
                item_id = int(line)
                match_list = self.get_match_list(item_id)
                if match_list:
                    print("item: %d, get matching list: %s" % (item_id, match_list))


clothes_matching_system = ClotheMatchingSystem()
# clothes_matching_system.test_items()  # 1417 is a test example, should return "160870;3118604"

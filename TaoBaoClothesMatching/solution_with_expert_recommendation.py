class ClotheMatchingSystem:
    def __init__(self):
        pass

    def is_in_list(self, item_id, clothe_list):
        clothes = clothe_list.split(",")
        for clothe_id in clothes:
            if item_id == int(clothe_id):
                return True
        return False

    def get_match_list(self, item_id):
        with open("./data/dim_fashion_matchsets.txt") as input_file:
            for line in input_file:
                tmp_line_arr_1 = line.split(" ")
                match_list = tmp_line_arr_1[1]
                tmp_line_arr_2 = match_list.split(";")
                target_index = -1
                result_list = ""
                for idx, clothes in enumerate(tmp_line_arr_2):
                    if self.is_in_list(item_id, clothes):
                        target_index = idx
                    else:
                        result_list = (result_list + clothes + ";")
                if target_index == -1:
                    return ""
                else:
                    return result_list[:-1]

    def test_items(self):
        with open("./data/test_items.txt") as input_file:
            for line in input_file:
                item_id = int(line)
                match_list = self.get_match_list(item_id)
                if match_list:
                    print("item: %d, get matching list: %s" % (item_id, match_list))


clothes_matching_system = ClotheMatchingSystem()
clothes_matching_system.test_items()  # 1417 is a test example, should return "160870;3118604"

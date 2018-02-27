with open("./data/dim_fashion_matchsets.txt") as input_file:
    for line in input_file:
        tmp_line_arr_1 = line.split(" ")
        match_id = int(tmp_line_arr_1[0])
        match_list = tmp_line_arr_1[1]
        if match_id == 1:
            tmp_line_arr_2 = match_list.split(";")
            print("match id: %d" % match_id)
            for clothes in tmp_line_arr_2:
                print("clothes: %s" % clothes)


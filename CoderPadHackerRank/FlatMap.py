# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dots menu on the tab, or add a new language
# tab using the Languages button on the left.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!

# AP - LC 341
# https://github.com/yao23/Machine_Learning_Playground/blob/master/LeetCode/341_flatten_nested_list_iterator.py
# https://www.youtube.com/watch?v=4ILiBgLokM8


# input: [1, [2], [[4, 3, 5]], 6, 7, 8, 9]

# output: [1, 2, 4, 3, 5, 6, 7, 8, 9]

def solution(input):
    output = []

    def dfs(element):
        # res = []
        if type(element) is list:
            for e in element:
                # res.append(dfs(e))
                dfs(e)
        else:
            # res.append(element)
            # return res
            output.append(element)

    for element in input:
        tmp = dfs(element)
        # if tmp:
        #     for t in tmp:
        #         output.append(t)
    return output

input = [1, [2], [[4, 3, 5]], 6, 7, 8, 9]
output = solution(input)
print(output)

import string

# def depth(tree):
#     if len(tree) == 1:
#         return 1
#     lst = list(tree.keys())
#     return len(tree) + depth(tree[lst[1]])

# four_level_tree = {"data": 54, "right_child": {"data": 93, "left_child": {"data": 63, "left_child": {"data": 59}}}}
 

# # HELPER FUNCTION TO BUILD TREES
# def build_bst(my_list):
#     if len(my_list) == 0:
#         return None

#     mid_idx = len(my_list) // 2
#     mid_val = my_list[mid_idx]

#     tree_node = {"data": mid_val}
#     tree_node["left_child"] = build_bst(my_list[ : mid_idx])
#     tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

#     return tree_node

# # HELPER VARIABLES
# tree_level_1 = build_bst([1])
# tree_level_2 = build_bst([1, 2, 3])
# tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# # test cases
# print(depth(tree_level_1) == 1)
# print(depth(tree_level_2) == 2)
# print(depth(tree_level_4) == 4)

# def build_shift_dict(shift):
#     letters_ref = string.ascii_uppercase + string.ascii_letters + string.ascii_lowercase
#     letters_shifted = {}
#     for i in range(26, 78):
#         letters_shifted[letters_ref[i]] = letters_ref[i + shift]
#     return letters_shifted

# def apply_shift(shift, message):
#     assert shift < 27, 'Shift must be from 0-26'
#     shifted_dict = build_shift_dict(shift)
#     message_text_new = ''
#     for i in message:
#         if i not in string.ascii_letters:
#             message_text_new += i
#         else:
#             message_text_new += shifted_dict[i]
#     return message_text_new

# print((apply_shift(1, 'Hello my name is guy!')).split(' '))

letters_ref = string.ascii_lowercase + string.ascii_letters + string.ascii_uppercase

print(letters_ref[78])
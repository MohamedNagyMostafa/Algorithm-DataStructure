from collections import namedtuple


def knapsack_max_value(max_weight, items):
    items   = sorted(items, key = lambda x: x.weight)
    print(items)
    lookup_table    = [0 for _ in range(max_weight + 1)]
    unused_items    = []
    for item in items:
        if item[0] > max_weight:
            break
        is_used = False
        weight  = 0
        for i in range(item[0], len(lookup_table)):
            if lookup_table[weight] + item[1] > lookup_table[i]:
                lookup_table[i] = lookup_table[weight] + item[1]
                is_used = True
            weight = (weight + 1) if weight + 1 < item[0] else weight

        if not is_used:
            unused_items.append(item)

    for item in unused_items:
        lookup_table[max_weight - item[0]] += item[1]
        if lookup_table[max_weight - item[0]] > lookup_table[-1]:
            lookup_table[-1] = lookup_table[max_weight - item[0]]

    print(unused_items)
    print(lookup_table)
    return lookup_table[-1]


# def knapsack_max_value(max_weight, items):
#     items   = sorted(items, key = lambda x: x.weight)
#
#     lookup_table    = [0 for _ in range(max_weight + 1)]
#     not_used_items  = []
#
#     for item in items:
#         if item[0] > max_weight:
#             continue
#         if item[1] > lookup_table[item[0]]:
#             lookup_table[item[0]:] = [item[1]] * len(lookup_table[item[0]:])
#         else:
#             not_used_items.append(item)
#     for item in not_used_items:
#         if item[0] > max_weight:
#             continue
#         for weight, value in enumerate(lookup_table):
#             if item[0] == weight:
#                 continue
#             if item[0] + weight > max_weight:
#                 break
#             if item[1] + value > lookup_table[item[0] + weight]:
#                 lookup_table[item[0] + weight] = item[1] + value
#
#     print(lookup_table)
#     return lookup_table[-1]

Item        = namedtuple('Item', ['weight', 'value'])

items       = [Item(10, 7), Item(9, 8), Item(5, 6)]
max_weight  = 15

max_value = knapsack_max_value(max_weight= max_weight, items= items)

print(f'Max value of items:{items} in knapsack weight {max_weight} is {max_value}')

items       = [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]
max_weight  = 25

max_value = knapsack_max_value(max_weight= max_weight, items= items)

print(f'Max value of items:{items} in knapsack weight {max_weight} is {max_value}')

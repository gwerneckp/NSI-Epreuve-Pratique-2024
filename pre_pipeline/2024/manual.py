from convert import transform_repl_into_unittest

first = """>>> recherche([2, 3, 4, 5, 6], 5)
3
>>> recherche([2, 3, 4, 6, 7], 5)
None"""


print(transform_repl_into_unittest(first))

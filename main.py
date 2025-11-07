def has_duplicates(lst)
    return len(lst) !=len(set(lst)
test_cases=[
    [1,2,3,4,5],
    [1,2,3,4,5],
    ["a","b","c","a"],
    []
]
for case in test_cases:
    result=has_duplicates(case)
    print(f"列表{case}{'有'if result else'无'} 重复元素")

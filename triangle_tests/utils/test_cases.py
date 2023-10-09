test_cases = [
    (
        (12, 14, 16),
        "scalene"
    ),
    (
        (12, 14, 14),
        "isosceles"
    ),
    (
        (12, 12, 12),
        "equilateral"
    ),

    (
        ("not_valid", 8, 12),
        "invalid_arguments"
    ),
    (
        (0, 14, 16),
        "not_triangle"
    ),
    (
        (12, 14, 38),
        "not_triangle"
    )
]


# test_cases = (
#     "triangles": [
#         (
#              (12, 14, 16),
#              "scalene"
#         ),
#         (
#              (12, 14, 14),
#              "isosceles"
#         ),
#         (
#              (12, 12, 12),
#              "equilateral"
#         )
#     ],
#     "wrong_type_of_arguments": [
#         (
#              ("not_valid", 8, 12),
#              "invalid_arguments"
#         ),
#     ],
#     "not_triangles": [
#         (
#              (0, 14, 16),
#              "not_triangle"
#         ),
#         (
#              (12, 14, 38),
#              "not_triangle"
#         )
#     ]
# )

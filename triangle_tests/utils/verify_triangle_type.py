from utils.is_triangle import is_triangle
from utils.has_adequate_arguments import has_adequate_arguments


def verify_triangle_type(side1: float, side2: float, side3: float) -> str:
    if (
        not has_adequate_arguments([side1, side2, side3], int, float)
    ):
        return "invalid_arguments"

    if (not is_triangle(side1, side2, side3)):
        return "not_triangle"

    is_isosceles = (side1 == side2 and side1 != side3) or (
        side3 == side2 and side1 != side3) or (side1 == side3 and side1 != side2)

    if is_isosceles:
        return "isosceles"

    is_equilateral = side1 == side2 == side3

    if (is_equilateral):
        return "equilateral"

    return "scalene"

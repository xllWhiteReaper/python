def is_triangle(side1: float, side2: float, side3: float) -> bool:
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False

    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else:
        return False

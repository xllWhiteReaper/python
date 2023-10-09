from utils.tex_utils import print_n_new_lines, print_red, print_green
from utils.verify_triangle_type import verify_triangle_type
from utils.test_cases import test_cases


def main() -> None:
    for index, (side_values, expected_return_value) in enumerate(test_cases):
        try:
            triangle_type = verify_triangle_type(*side_values)
            print(
                f"Expected value: {expected_return_value}, returned value: {triangle_type}")
            test_success = expected_return_value == triangle_type

            print_green(f"Test number {index+1} passed successfully") if test_success else print_red(
                f"Test number {index+1} failed")
            print_n_new_lines(2)
        except:
            print(f"Error in test {index+1}")


if __name__ == "__main__":
    main()

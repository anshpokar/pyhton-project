# # import geometry
# #
# # def pointyShapeVolume(x, h, square):
# #     if square:
# #         base = geometry.squareArea(x)  # Calculates the area of a square.
# #     else:
# #         base = geometry.circleArea(x)  # Calculates the area of a circle.
# #     return h * base / 3.0  # Volume of a pyramid or cone.
# #
# # print(dir(geometry))  # Lists the available functions in the geometry module.
# # print(pointyShapeVolume(4, 2.6, True))  # For a square base.
# # print(pointyShapeVolume(4, 2.6, False))  # For a circular base.
#
#
# import geometry
#
# print(dir(geometry))
#
#
# def pointyShapeVolume(x, y, squareBase):
#     if squareBase:
#         base_area = geometry.squareArea(x)
#     else:
#         base_area = geometry.circleArea(x)
#
#     volume = (1 / 3) * base_area * y
#     return volume
#
#
# # Example usage:
# print("Volume of square pyramid:", pointyShapeVolume(4, 9, True))
# print("Volume of circular cone:", pointyShapeVolume(3, 9, False))


def divide_numbers():
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        print(f"Result: {numerator / denominator}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    finally:
        print("Execution complete.")

divide_numbers()


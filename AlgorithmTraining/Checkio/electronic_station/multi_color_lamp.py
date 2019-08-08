"""
Your task is to create the class Lamp() and method light() which will make the lamp glow with one of the four colors in the sequence - (‘Green’, ‘Red’, ‘Blue’, ‘Yellow’).
When the light() method is used for the first time,
the color should be "Green", the second time - "Red" and so on.
If the current color is "Yellow", the next color should be "Green" and so on. In this mission you can use the State design pattern.

Input: A few strings indicating the number of times the lamp is being turned on.
Output: The color of the lamp.
"""

class Lamp:
    LIGHT = ["Green", "Red", "Blue", "Yellow"]

    def __init__(self):
        self.current = 0

    def light(self):
        light = self.LIGHT[self.current % 4]
        self.current += 1
        return light


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")

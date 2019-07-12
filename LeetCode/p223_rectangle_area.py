# P223 Rectangle Area
# Medium

# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.


# Note:
# Assume that the total area is never beyond the maximum possible value of int.


class Solution(object):

    # Determine the corner coor in each other and with help of boundary location
    # Use multile conditions to determine the overlap
    def isIn(self, coor, rec):
        """
        To determine whether a coor in inside or on the fringe of a rectangular
        coor is a tuple of two numbers.
        rec is represented with a list of 4 coor of the 4 corner
        """
        x, y = coor[0], coor[1]
        top, bottom, left, right = rec[1][1], rec[0][1], rec[0][0], rec[1][0]
        # print(top, bottom, left, right)
        if left <= x <= right and  bottom <= y <= top:
            return True
        else:
            return False

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        (A,B), (C,D) - first rectangular
        (E,F), (G,H) - second rectagular
        """
        R1 = [(A,B), (C,D), (A,D), (C,B)]
        R2 = [(E,F), (G,H), (E,H), (G,F)]
        R1_left, R1_top, R1_bot, R1_right = A, D, B, C
        R2_left, R2_top, R2_bot, R2_right = E, H, F, G

        A1 = abs(D-B) * (C-A)
        A2 = abs(H-F) * (G-E)

        R1_in = []
        for i in R1:
            if self.isIn(i, R2):
                R1_in.append(i)
        R1_in = sorted(R1_in)

        R2_in = []
        for i in R2:
            if self.isIn(i, R1):
                R2_in.append(i)
        R2_in = sorted(R2_in)

        def overlap(R1_in, R2_in):
            if len(R1_in) == 0 and len(R2_in) == 0:
                if R2_top > R1_top and R2_bot < R1_bot and R1_left < R2_left and R1_right > R2_right:
                    return (R2_right - R2_left) * (R1_top - R1_bot)
                elif R1_top > R2_top and R1_bot < R2_bot and R2_left < R1_left and R2_right > R1_right:
                    return (R1_right - R1_left) * (R2_top - R2_bot)
                else:
                    return 0

            elif len(R1_in) == 1 and len(R2_in) == 1:
                C1, C2 = R1_in[0], R2_in[0]
                overlap = abs(C1[0] - C2[0]) * abs(C1[1] - C2[1])
                return overlap

            elif len(R1_in) == 2:
                R1a, R1b = R1_in[0], R1_in[1]
                xa, ya, xb, yb = R1a[0], R1a[1], R1b[0], R1b[1]
                if xa == xb:
                    h = abs(ya - yb)
                    if R2_left < R1_right < R2_right:
                        w = R1_right - R2_left
                    elif R2_left < R1_left < R2_right:
                        w = R2_right - R1_left
                    elif R1_left < R2_left < R1_right:
                        w = R1_right - R2_left
                    elif R1_left < R2_right < R1_right:
                        w = R2_right - R1_left
                    else:
                        w = 0
                    return h * w
                if ya == yb:
                    w = abs(xa - xb)
                    if R2_bot < R1_bot < R2_top:
                        h = R2_top - R1_bot
                    elif R2_bot < R1_top < R2_top:
                        h = R1_top - R2_bot
                    elif R1_bot < R2_bot < R1_top:
                        h = R1_top - R2_bot
                    elif R1_bot < R2_top < R1_top:
                        h = R2_top - R1_bot
                    else:
                        h = 0
                    return h * w

            elif len(R2_in) == 2:
                R2a, R2b = R2_in[0], R2_in[1]
                xa, ya, xb, yb = R2a[0], R2a[1], R2b[0], R2b[1]
                if xa == xb:
                    h = abs(ya - yb)
                    if R1_left < R2_left < R1_right:
                        w = R1_right - R2_left
                    elif R1_left < R2_right < R1_right:
                        w = R2_right - R1_left
                    elif R2_left < R1_left < R2_right:
                        w = R2_right - R1_left
                    elif R2_left < R1_right < R2_right:
                        w = R1_right - R2_left
                    else:
                        w = 0
                    return h * w
                if ya == yb:
                    w = abs(xa - xb)
                    if R1_bot < R2_top < R1_top:
                        h = R2_top - R1_bot
                    elif R1_bot < R2_bot < R1_top:
                        h = R1_top - R2_bot
                    elif R2_bot < R1_top < R2_top:
                        h = R1_top - R2_bot
                    elif R2_bot < R1_bot < R2_top:
                        h = R2_top - R1_bot
                    else:
                        h = 0
                    return h * w

            elif len(R1_in) == 4:
                return A1
            elif len(R2_in) == 4:
                return A2

        return A1 + A2 - overlap(R1_in, R2_in)


if __name__ == "__main__":
    assert Solution().computeArea(0, 0, 1, 0, 2, 0, 3, 0) == 0, "Edge 1, horizontal line"
    assert Solution().computeArea(0, 0, 0, 1, 0, 2, 0, 3) == 0, "Edge 2, vertical line"

    assert Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45, "Example 1"

    assert Solution().computeArea(-2, -2, 2, 2, -2, -4, 2, -2) == 24, "Additional 1"
    assert Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2) == 16, "Additional 2"
    assert Solution().computeArea(-5, -5, -3, 3, -3, -3, 3, 3) == 52, "Additional 3"
    assert Solution().computeArea(-5, -3, 3, 0, -3, -3, 3, 3) == 42, "Additional 4"
    assert Solution().computeArea(-5, -2, 5, 1, -3, -3, 3, 3) == 48, "Additional 5"
    assert Solution().computeArea(-5, -5, -4, 5, -3, -3, 3, 3) == 46, "Additional 6"

    print("all passed")

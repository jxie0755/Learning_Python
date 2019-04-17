class MergeSort:

    def sort(self, lst):
        container = [[i] for i in lst]
        if not container:
            return []
        while len(container) != 1:
            l1 = container.pop(0)
            l2 = container.pop(0)
            container.append(self.merge(l1, l2))
        return container[0]



    def merge(self, l1, l2):
        """merge two sorted list"""
        i, j = 0, 0
        N1, N2 = len(l1), len(l2)
        result = []
        while i < N1 or j < N2:
            if i == N1:
                result += l2[j:]
                j = N2
            elif j == N2:
                result += l1[i:]
                i = N1
            else:
                c1, c2 = l1[i], l2[j]
                if l1[i] <= c2:
                    result.append(c1)
                    i += 1
                elif c1 > c2:
                    result.append(c2)
                    j += 1
        return result

if __name__ == '__main__':
    a = [10,9,1,6,7,3,5,3,4,8,2,2,1]
    assert MergeSort().sort(a) == [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10], 'Example 1'

    a = []
    assert MergeSort().sort(a) == [], 'Edge 1'

    a = [1]
    assert MergeSort().sort(a) == [1], 'Edge 2'

    a = [1,1,1]
    assert MergeSort().sort(a) == [1, 1, 1], 'Edge 3'

    print('all passed')

class FlatIterator:

    def __init__(self, self_lst):
        self.lst = self_lst
        self.i = 0
        self.j = 0

        self.isTrue_j = True
        self.is_res = False

        self.res = None

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if not isinstance(self.lst[self.i], list):
                self.res = self.lst[self.i]
                self.i += 1
                self.is_res = True
            else:
                self.isTrue_j = True
                while self.isTrue_j:
                    try:
                        self.res = self.lst[self.i][self.j]
                        self.is_res = True
                        try:
                            s = self.lst[self.i][self.j + 1]
                            self.j += 1
                        except IndexError:
                            self.i += 1
                            self.j = 0
                            self.isTrue_j = False
                        break
                    except IndexError:
                        pass
        except IndexError:
            raise StopIteration
        if self.is_res:
            self.is_res = False
            return self.res

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

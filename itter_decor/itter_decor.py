class FlatIterator:

    def __init__(self, list_of_list):
        self.done_list = []
        self.index = 0

        for parent_list in list_of_list:
            for item in parent_list:
                self.done_list.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.done_list):
            raise StopIteration

        item = self.done_list[self.index]

        self.index += 1

        return item


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

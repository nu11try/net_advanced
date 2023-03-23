class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def balance(text):
    closing = [')', '}', ']']
    opening = ['(', '{', '[']

    stack = Stack()

    for char in text:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            elif opening.index(stack.peek()) == closing.index(char):
                stack.pop()
            else:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    assert balance('(((([{}]))))') is True
    assert balance('[([])((([[[]]])))]{()}') is True
    assert balance('{{[()]}}') is True

    assert balance('}{}') is False
    assert balance('{{[(])]}}') is False
    assert balance('[[{())}]') is False

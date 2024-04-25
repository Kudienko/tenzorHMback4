class Stack:
    def __init__(self):
        self.items = []

    def last(self):
        if not self.check():
            return self.items[-1]
        return None

    def check(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def delete(self):
        if not self.check():
            return self.items.pop()
        return None

def check_brackets(text):
    stack = Stack()
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for index, char in enumerate(text, 1):
        # Если встречается открывающая скобка, она добавляется в стек.
        if char in brackets.keys():
            stack.put((char, index))
        # Если встречается закрывающая скобка, она сравнивается с последней открывающей скобкой в стеке.
        elif char in brackets.values():
            # Если скобки не совпадают или стек пуст, функция возвращает индекс текущей скобки.
            if stack.check() or brackets[stack.last()[0]] != char:
                return index
            stack.delete()
    # Если стек пуст, функция возвращает "Success", иначе возвращает индекс последней открывающей скобки в стеке.
    if stack.check():
        return 'Success'
    else:
        return stack.last()[1]


if __name__ == '__main__':
    input = input().strip()
    print(check_brackets(input))



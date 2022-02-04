class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def check(elements, sequence):
    control = Stack()
    flag = 'Сбалансированно'
    for el in sequence:
        if el in elements:
            control.push(el)
        elif el == elements.get(control.peek()):
            control.pop()
        else:
            return 'Несбалансированно'
    return flag if control.isEmpty() else 'Несбалансированно'

if __name__ == '__main__':
    ELEMENTS = {'(':')', '[':']', '{':'}'}
    SEQUENCE = [')))[]', '()()()))', '(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for el in SEQUENCE:
        print(check(ELEMENTS, el))

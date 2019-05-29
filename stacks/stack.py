

class StackEmpty(Exception):
    """Error to access data from empty stack"""
    pass


class ArrayStack():

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise StackEmpty('Empty Stack')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise StackEmpty('Empty Stack')
        self._data.pop()

if __name__ == '__main__':
    # Matching Parentheses

    # True, True, False, F, F
    test = ['()(()){([()])}', '((()(()){([()])}))', ')(()){([()])}', '({[])}', '(']
    res = [False] * len(test)
    match = {')': '(', ']': '[', '}': '{'}
    for i, t in enumerate(test):
        s = ArrayStack()
        flag = 0
        for c in t:
            if c == '(' or c =='[' or c == '{':
                s.push(c)
            elif c == ')' or c == ']' or c == '}':
                if len(s) == 0:
                    flag = 1
                    break
                if match[c] == s.top():
                    s.pop()
                else:
                    s.push(c)
            else:
                flag = 1
                break

        if len(s) == 0 and flag == 0:
            res[i] = True
    print(res)

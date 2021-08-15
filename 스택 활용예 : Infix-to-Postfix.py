class Stack:
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return self.__len__() == 0
def infix_to_postfix(infix):

    opstack = Stack()
    outstack=[]
    token_list = infix.split()

    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3
    for token in token_list:
        if token =='(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
        elif token in '+-*/^':
            if opstack.isEmpty()==True:
                opstack.push(token)
            elif prec[token]>prec[opstack.top()]:
                opstack.push(token)
            else:
                while prec[opstack.top()]>= prec[token]:
                    outstack.append(opstack.pop())
                    if opstack.isEmpty() == True:
                        break
                opstack.push(token)
        else:
            outstack.append(token)
    #opstack에 남은 모든 연산자를 pop한 후 outstack에 append
    while opstack.isEmpty() ==False:
        outstack.append(opstack.pop())
    return " ".join(outstack)

infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)

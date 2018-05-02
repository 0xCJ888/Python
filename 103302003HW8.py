
class Calculator:
    def __init__(self,stack):
        self.infix = ''
        self.stack = stack
    def validch(self):
        validExp = ''
        for x in self.stack:
            if x == ' ':
                continue
            if self.__is__digit(x) or self.__is_operators(x) or x == '.':
                validExp += x
            else:
                print('Syntax error')
                return 
        self.infix = validExp
        return True
    def toPostfix(self):
        opStack = []
        postfix = ''
        tmp = 0
        if self.__is_operators(self.infix[0]):
            self.infix = '0'+ self.infix
        for x in self.infix:
            if self.__is_operators(x) and self.__is_operators(tmp):
                postfix += x
                continue
            if self.__is__digit(x) or x == '.':
                postfix += x
            elif self.__is_operators(x):
                if len(opStack) == 0:
                    opStack.append(x)
                    postfix += ' '
                else:
                    if self.__is_priority(x) > self.__is_priority(opStack[-1]):
                        opStack.append(x)
                        postfix += ' '
                    else:
                        postfix += ' ' + opStack.pop() + ' '
                        opStack.append(x)
            tmp = x
        while(len(opStack)!= 0):
            postfix += ' '+ opStack.pop() + ' '
        p = postfix.split()
        return p
    def calc_postfix(self, postfix):
        stack = []
        for x in postfix:
            stack.append(x)
            if self.__is_operators(x):
                op = stack.pop()
                num2 = stack.pop()
                num1 = stack.pop()
                if not self.__is_float(num1) or not self.__is_float(num2):
                    print('Syntax error')
                    return 
                else:
                    value = self.calc(op, float(num1), float(num2))
                    stack.append(str(value))
        return stack[0]
    @staticmethod
    def calc(op, p1, p2):
        if op == '+':
            return p1 + p2
        elif op == '-':
            return p1 - p2
        elif op == '*':
            return p1 * p2
        elif op == '/':
            if(p2 == 0):
                print('error')
                return 
            return p1 / p2                
    @staticmethod
    def __is_operators(text):
        return text in {'+', '-', '*', '/'}
    @staticmethod
    def __is__digit(text):
        return text.isdigit()
    @staticmethod
    def __is_float(text):
        flag = True
        try:
            float(text)
        except ValueError:
            flag = False
        return flag
    @staticmethod
    def __is_priority(op):
        if op in {'+', '-'}:
            return 1
        elif op in {'*', '/'}:
            return 2
        else:
            return 0

while(1):
    s = input('>')
    if(s == 'exit' or s == 'quit'):
        break
    calc = Calculator(s)
    isValid = calc.validch()
    if isValid:
        p = calc.toPostfix()
        output = calc.calc_postfix(p)
        if output:
            print(output)
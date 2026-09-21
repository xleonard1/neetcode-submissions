class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack = []
    
        for token in tokens:

            if token == '+':
                total = eval_stack.pop() + eval_stack.pop()
                eval_stack.append(total)
            elif token == '-':
                recently_added = eval_stack.pop()
                previously_added = eval_stack.pop()
                total = previously_added - recently_added

                eval_stack.append(total)
            elif token == '*':
                total = eval_stack.pop() * eval_stack.pop()
                eval_stack.append(total)
            elif token == '/':
                recently_added = eval_stack.pop()
                previously_added = eval_stack.pop()
                total = int(previously_added / recently_added)

                eval_stack.append(total)
            else:
                eval_stack.append(int(token))

        return eval_stack[0]
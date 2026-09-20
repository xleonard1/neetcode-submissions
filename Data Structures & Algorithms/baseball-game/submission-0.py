class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i, operation in enumerate(operations):
            if operation.lstrip('-').isdigit():
                num = int(operation)
                record.append(num)
            elif operation == '+':
                last_score = record[-1]
                last_before_last_score = record[-2]
                record.append(last_score + last_before_last_score)
            elif operation == 'D':
                previous_score = record[-1]
                record.append(previous_score * 2)
            elif operation == 'C':
                record.pop()
                
        return sum(record)
    


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for i, operation in enumerate(operations):
            if operation == '+':
                last_score = records[-1]
                last_before_last_score = records[-2]
                records.append(last_score + last_before_last_score)
            elif operation == 'D':
                previous_score = records[-1]
                records.append(previous_score * 2)
            elif operation == 'C':
                records.pop()
            else:
                records.append(int(operation))
                
        return sum(records)
    


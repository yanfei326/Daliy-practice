#8、字符串转换整数（atoi）
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = 'start'#当前状态
        self.sign = 1#正负号
        self.ans = 0#累积的数字结果
        self.table = {  #0         1          2          3   状态转移表。行：当前状态；列：字符类型
            'start': ['start', 'signed', 'in_number', 'end'],#start刚开始，遇到空格进入start，遇到符号进入signed，遇到数字进入in_number，遇到其他情况进入end
            'signed': ['end', 'end', 'in_number', 'end'],#已经读到符号，遇到空格进入end，遇到符号进入end，遇到数字进入in_number，遇到其他情况进入end
            'in_number': ['end', 'end', 'in_number', 'end'],#正在读数字，遇到空格进入end，遇到符号进入end，遇到数字进入in_number，遇到其他情况进入end
            'end': ['end', 'end', 'end', 'end'],#结束了，遇到任何情况都是end，不再产生变化
        }
        
    def get_col(self, c):#判断字符类型
        if c.isspace():
            return 0#遇空格
        if c == '+' or c == '-':
            return 1#遇符号
        if c.isdigit():
            return 2#遇数字
        return 3#遇其他

    def get(self, c):#读一个字符并更新状态
        self.state = self.table[self.state][self.get_col(c)]#当前状态（根据上一个字符确定）+要转移的列号（根据这个位置上的字符确定）
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)#截断处理
        elif self.state == 'signed':              #elif否则如果，表示如果if条件不成立时，再判断另一个条件
            self.sign = 1 if c == '+' else -1

class Solution:#主函数
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()#创建自动机
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans#符号×绝对值=最终结果

    #"  -00123a5"
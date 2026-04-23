def 计算(数值列表: list, 总数: int = 24, 处理函数: callable = None) -> list[list[str]]:
    所有解法 = []
    已探索路径 = set() # 记录已探索的状态以避免重复计算
    
    def _计算所有(当前数值列表, 计算步骤: list[str]):
        # 创建状态的哈希表示
        状态 = (tuple(sorted(当前数值列表)), tuple(sorted(计算步骤)))
        if 状态 in 已探索路径:
            return
        已探索路径.add(状态)
        
        if len(当前数值列表) == 1:
            if abs(当前数值列表[0] - 总数) < 1e-10:
                计算步骤2 = 计算步骤.copy()
                所有解法.append(计算步骤2)
                if 处理函数:
                    处理函数(计算步骤2)
            return
            
        长度 = len(当前数值列表)
        
        for _1 in range(长度):
            for _2 in range(长度):
                if _1 == _2: 
                    continue
                    
                数值1 = 当前数值列表[_1]
                数值2 = 当前数值列表[_2]
                
                # 生成剩余数值列表
                剩余数值列表 = [当前数值列表[i] for i in range(长度) if i not in (_1, _2)]
                
                # 尝试所有运算符
                for 运算符 in ['+', '-', '*', '/']:
                    # 加法和乘法：只尝试一种顺序（因为满足交换律）
                    if 运算符 in ['+', '*'] and 数值1 > 数值2:
                        continue
                    
                    表达式 = f'{数值1} {运算符} {数值2}'
                    try: 
                        结果 = eval(表达式)
                    except ZeroDivisionError: 
                        continue
                    
                    # 处理浮点数精度
                    if isinstance(结果, float):
                        if abs(结果 - round(结果)) < 1e-10:
                            结果 = round(结果)
                    
                    当前步骤 = f'{数值1} {运算符} {数值2} = {结果}'
                    _计算所有([结果] + 剩余数值列表, 计算步骤 + [当前步骤])
                    
                    # 对于减法和除法, 如果数值不同, 尝试另一种顺序
                    if 运算符 in ['-', '/'] and 数值1 != 数值2:
                        表达式 = f'{数值2} {运算符} {数值1}'
                        if 运算符 == '-':
                            try: 
                                结果 = eval(表达式)
                            except ZeroDivisionError: 
                                continue
                            
                            if isinstance(结果, float):
                                if abs(结果 - round(结果)) < 1e-10:
                                    结果 = round(结果)
                            
                            当前步骤 = f'{数值2} {运算符} {数值1} = {结果}'
                            _计算所有([结果] + 剩余数值列表, 计算步骤 + [当前步骤])
    
    _计算所有(数值列表, [])
    
    return 所有解法

if __name__ == '__main__':
    列表 = [1, 2, 3, 4, 5, 6]
    目标 = 1

    def 处理函数(计算步骤: list[str]):
        print(', '.join(计算步骤))

    计算(列表, 目标, 处理函数)
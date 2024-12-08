from random import randint
from math import prod
from math import exp as math_exp, log as math_log
from math import sin as math_sin, cos as math_cos

class NaiveGraph:
    
    node_list = [] # 图节点列表
    id_list = []   # 节点ID列表

    operator_calculate_table = {
        "add": lambda node: sum([last.get_value() for last in node.last]),
        "mul": lambda node: prod([last.get_value() for last in node.last]),
        "div":
        lambda node: node.last[0].get_value() / node.last[1].get_value(),
        "sub":
        lambda node: node.last[0].get_value() - node.last[1].get_value(),
        "exp": lambda node: math_exp(node.last[0].get_value()),
        "log": lambda node: math_log(node.last[0].get_value()),
        "sin": lambda node: math_sin(node.last[0].get_value()),
        "cos": lambda node: math_cos(node.last[0].get_value()),
    }
    class Node:
        def __init__(self, name) -> None:
            # 生成唯一的节点id
            while True:
                new_id = randint(0, 1000)
                if new_id not in NaiveGraph.id_list:
                    break
            self.id: int = new_id
            self.name = name

            self.next = list() # 节点指向的节点列表
            self.last = list() # 指向节点的节点列表
            self.in_deg, self.in_deg_com = 0, 0 # 节点入度
            self.out_deg, self.out_deg_com = 0, 0 # 节点出度
            NaiveGraph.add_node(self)
            
        def build_edge(self, node):
            # 构建self节点与node节点的有向边
            self.out_deg += 1
            node.in_deg += 1
            self.next.append(node)
            node.last.append(self)

    @classmethod
    def add_node(cls, node):
        # 在计算图中加入节点
        cls.node_list.append(node)
        cls.id_list.append(node.id)

    @classmethod
    def clear(cls):
        # 刷新计算图
        cls.node_list.clear()
        cls.id_list.clear()

    class Constant(Node):
        def __init__(self, value, name) -> None:
            super().__init__(name)
            self.__value = float(value)

        def get_value(self):
            return self.__value

        def __repr__(self) -> str:
            return str(self.__value)

    class Variable(Node):
        def __init__(self, value, name) -> None:
            super().__init__(name)
            self.value = float(value)
            self.grad = 0.

        def get_value(self):
            return self.value

        def __repr__(self) -> str:
            return str(self.value)

    class PlaceHolder(Node):
        def __init__(self, name) -> None:
            super().__init__(name)
            self.value = None
            self.grad = 0.

        def get_value(self):
            return self.value

        def __repr__(self) -> str:
            return str(self.value)


    class Operator(Variable):
        def __init__(self, operator: str) -> None:
            super().__init__(0, operator)
            self.operator = operator
            self.calculate = NaiveGraph.operator_calculate_table[operator]

        def __repr__(self) -> str:
            return self.operator
    @classmethod
    def binary_function_frame(cls, node1, node2, operator):
        '''
        一般的二元函数框架
        '''
        if not isinstance(node1, NaiveGraph.Node):
            node1 = NaiveGraph.Constant(node1)
        if not isinstance(node2, NaiveGraph.Node):
            node2 = NaiveGraph.Constant(node2)
        node_operator = NaiveGraph.Operator(operator)
        node1.build_edge(node_operator)
        node2.build_edge(node_operator)
        return node_operator
    
    @classmethod
    def unary_function_frame(cls, node, operator):
        if not isinstance(node, NaiveGraph.Node):
            node = NaiveGraph.Constant(node)
        node_operator = NaiveGraph.Operator(operator)
        node.build_edge(node_operator)
        return node_operator


    @classmethod
    def commutable_binary_function_frame(cls, node1, node2, operator):
        if not isinstance(node1, NaiveGraph.Node):
            node1 = NaiveGraph.Constant(node1)
        if not isinstance(node2, NaiveGraph.Node):
            node2 = NaiveGraph.Constant(node2)

        if isinstance(
                node1,
                NaiveGraph.Operator,
        ) and node1.operator == operator:
            node2.build_edge(node1)
            return node1
        elif isinstance(
                node2,
                NaiveGraph.Operator,
        ) and node2.operator == operator:
            node1.build_edge(node2)
            return node2
        else:
            node_operator = NaiveGraph.Operator(operator)
            node1.build_edge(node_operator)
            node2.build_edge(node_operator)
            return node_operator


    @classmethod
    def add(cls, node1, node2):
        return NaiveGraph.associative_binary_function_frame(
            node1, node2, "add")

    @classmethod
    def sub(cls, node1, node2):
        return NaiveGraph.binary_function_frame(node1, node2, "sub")

    @classmethod
    def exp(cls, node1):
        return NaiveGraph.unary_function_frame(node1, "exp")


    @classmethod
    def forward(cls):
        node_queue = [] # 节点队列
        
        for node in cls.node_list:
            # 入度为0的节点入队
            if node.in_deg == 0:
                node_queue.append(node)

        while len(node_queue) > 0:
            node = node_queue.pop()
            for next_node in node.next:
                next_node.in_deg -= 1
                next_node.in_deg_com += 1
                if next_node.in_deg == 0:
                    next_node.value = next_node.calculate(next_node)
                    node_queue.insert(0, next_node)

        for node in cls.node_list:
            node.in_deg += node.in_deg_com
            node.in_deg_com = 0


    @classmethod
    def backward(cls):
        node_queue = []
        for node in cls.node_list:
            if node.out_deg == 0 and not isinstance(
                    node,
                    NaiveGraph.Constant,
            ):
                node.grad = 1.
                node_queue.append(node)
        if len(node_queue) > 1:
            print('''
                计算图中的函数是多元输出，自动微分会计算梯度的和，
                如果要求指定输出的导数，应该是用backward_from_node。
                ''')

        while len(node_queue) > 0:
            node = node_queue.pop()
            for last_node in node.last:
                last_node.out_deg -= 1
                last_node.out_deg_com += 1
                if last_node.out_deg == 0 and not isinstance(
                        last_node,
                        NaiveGraph.Constant,
                ):  # 准备求导
                    for n in last_node.next:
                        assert n.operator != None
                        last_node.grad += n.grad * cls.__deriv(n, last_node)
                    node_queue.insert(0, last_node)

        for node in cls.node_list:
            node.out_deg += node.out_deg_com
            node.out_deg_com = 0
## TESTS ##

Constant = NaiveGraph.Constant
Variable = NaiveGraph.Variable
Operator = NaiveGraph.Operator

x = Constant(1, name='x')
y = Variable(2, name='y')

add = Operator("add")
x.build_edge(add)
y.build_edge(add)

exp = Operator("exp")
x.build_edge(exp)

graph = NaiveGraph()

gra

# Based on forward propagation, c: 42.63906
# Based on backward propagation, df/da: 4.07143
# Based on backward propagation, df/db: 10.07143

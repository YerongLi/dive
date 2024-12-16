from random import randint

from math import prod, isclose
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
        def __init__(self, value) -> None:
            super().__init__('constant')
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
    def __deriv_add(cls, child: Operator, parent: Node):
        # ∂(a + b)/∂a = 1, ∂(a + b)/∂b = 1
        return 1.0

    @classmethod
    def __deriv_sub(cls, child: Operator, parent: Node):
        # ∂(a - b)/∂a = 1, ∂(a - b)/∂b = -1
        return 1.0 if parent is child.last[0] else -1.0

    @classmethod
    def __deriv_mul(cls, child: Operator, parent: Node):
        # ∂(a * b)/∂a = b, ∂(a * b)/∂b = a
        if parent is child.last[0]:  # Parent is 'a'
            return child.last[1].value  # Return 'b'
        elif parent is child.last[1]:  # Parent is 'b'
            return child.last[0].value  # Return 'a'
        else:
            raise ValueError("Parent node is not part of the multiplication operation.")

    @classmethod
    def __deriv_div(cls, child: Operator, parent: Node):
        # ∂(a / b)/∂a = 1/b, ∂(a / b)/∂b = -a/b^2
        if parent is child.last[0]:  # Parent is 'a'
            return 1.0 / child.last[1].value
        elif parent is child.last[1]:  # Parent is 'b'
            return -child.last[0].value / (child.last[1].value ** 2)
        else:
            raise ValueError("Parent node is not part of the division operation.")

    @classmethod
    def __deriv_exp(cls, child: Operator, parent: Node):
        # ∂(exp(a))/∂a = exp(a)
        return child.value  # e^a is the value of the child node

    @classmethod
    def __deriv_log(cls, child: Operator, parent: Node):
        # ∂(log(a))/∂a = 1/a
        if parent is child.last[0]:
            return 1.0 / parent.value
        else:
            raise ValueError("Parent node is not part of the logarithm operation.")
    @classmethod
    def __deriv(cls, child: Operator, parent: Node):
        return {
            "add": cls.__deriv_add,
            "sub": cls.__deriv_sub,
            "mul": cls.__deriv_mul,
            "div": cls.__deriv_div,
            "exp": cls.__deriv_exp,
            "log": cls.__deriv_log,
        }[child.operator](child, parent)

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

x = Constant(1)
y = Variable(2, name='y')

add = Operator("add")
x.build_edge(add)
y.build_edge(add)

exp = Operator("exp")
x.build_edge(exp)




graph = NaiveGraph()

NaiveGraph.clear()

# Step 1: Define variables a and b
a = Variable(4, name="a")
b = Variable(10, name="b")

# Step 2: Construct the computational graph
# Compute a * b
mul_ab = NaiveGraph.binary_function_frame(a, b, "mul")

# Compute a + b
add_ab = NaiveGraph.binary_function_frame(a, b, "add")

# Compute log(a + b)
log_add_ab = NaiveGraph.unary_function_frame(add_ab, "log")

# Compute f(a, b) = a * b + log(a + b)
f = NaiveGraph.binary_function_frame(mul_ab, log_add_ab, "add")

# Step 3: Perform forward propagation
NaiveGraph.forward()

f_value = f.get_value()
print(f"Value of f(a, b): {print(f_value)}")  # Should print the value of f(a, b)

expected_value = 42.6390573296
assert isclose(f_value, expected_value, rel_tol=1e-9), \
    f"Test failed: f(a, b) = {f_value}, expected {expected_value}"
# Step 4: Perform backward propagation
NaiveGraph.backward()
def dfda(a, b):
    """
    Partial derivative of f(a, b) with respect to a.
    """
    return b + 1 / (a + b)

def dfdb(a, b):
    """
    Partial derivative of f(a, b) with respect to b.
    """
    return a + 1 / (a + b)
expected_value = 42.6390573296

expected_a = dfda(a.value, b.value)
expected_b = dfdb(a.value, b.value)

# Print and assert
# print(f"Gradient w.r.t a: {a.grad}, Expected: {expected_a}")
assert isclose(a.grad, expected_a, rel_tol=1e-9), f"Mismatch in df/da: {a.grad} != {expected_a}"

# print(f"Gradient w.r.t b: {b.grad}, Expected: {expected_b}")
assert isclose(b.grad, expected_b, rel_tol=1e-9), f"Mismatch in df/db: {b.grad} != {expected_b}"
# Based on forward propagation, c: 42.63906
# Based on backward propagation, df/da: 4.07143
# Based on backward propagation, df/db: 10.07143
print("Test passed: f(a, b) is close to the expected value.")

# TEST 2


graph = NaiveGraph()

NaiveGraph.clear()

# Step 1: Define variables a and b
a = Variable(4, name="a")
b = Variable(10, name="b")

# f = exp(a - 3) / (b - 3)
# Step 2: Construct the computational graph
# Compute a - 3
sub_a3 = NaiveGraph.binary_function_frame(a, 3, "sub")

# Compute exp(a - 3)
exp_sub_a3 = NaiveGraph.unary_function_frame(sub_a3, "exp")

# Compute b - 3
sub_b3 = NaiveGraph.binary_function_frame(b, 3, "sub")

# Compute f(a, b) = exp(a - 3) / (b - 3)
f = NaiveGraph.binary_function_frame(exp_sub_a3, sub_b3, "div")

# Step 3: Perform forward propagation
NaiveGraph.forward()

f_value = f.get_value()
print(f"Value of f(a, b): {f_value}")  # Should print the value of f(a, b)

def dfda(a, b):
    """
    Partial derivative of f(a, b) with respect to a.
    """
    return math_exp(a - 3) / (b - 3)

def dfdb(a, b):
    """
    Partial derivative of f(a, b) with respect to b.
    """
    return -math_exp(a - 3) / ((b - 3) ** 2)

expected_value = math_exp(1) / 7  # exp(4 - 3) / (10 - 3)
assert isclose(f_value, expected_value, rel_tol=1e-9), \
    f"Test failed: f(a, b) = {f_value}, expected {expected_value}"
print("Test passed: f(a, b) is close to the expected value.")

# Step 4: Perform backward propagation
NaiveGraph.backward()
expected_a = dfda(a.value, b.value)
expected_b = dfdb(a.value, b.value)

# Print and assert
assert isclose(a.grad, expected_a, rel_tol=1e-9), f"Mismatch in df/da: {a.grad} != {expected_a}"
assert isclose(b.grad, expected_b, rel_tol=1e-9), f"Mismatch in df/db: {b.grad} != {expected_b}"

# Based on forward propagation, f(a, b): exp(1) / 7
# Based on backward propagation, df/da: exp(1) / 7
# Based on backward propagation, df/db: -exp(1) / 49


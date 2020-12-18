from collections import deque

ops = {
    '+': (lambda x, y: x + y),
    '*': (lambda x, y: x * y)
}

def solution(inp):
    tot = 0
    for line in inp:
        postfix = []
        st = deque()
        for tok in line:
            if tok == '(':
                st.append(tok)
            elif tok in ('1','2','3','4','5','6','7','8','9','0'):
                postfix.append(tok)
            elif tok == '+':
                while st and st[-1] != '(' and st[-1] != '*':
                    postfix.append(st[-1])
                    st.pop()
                st.append(tok)
            elif tok == '*':
                while st and st[-1] != '(':
                    postfix.append(st[-1])
                    st.pop()
                st.append(tok)
            elif tok == ')':
                while st and st[-1] != '(':
                    postfix.append(st[-1])
                    st.pop()
                st.pop()
        while len(st) > 0:
            postfix.append(st[-1])
            st.pop()
        st2 = deque()
        for tok in postfix:
            if tok in ('1','2','3','4','5','6','7','8','9','0'):
                st2.append(int(tok))
            else:
                op1 = st2.pop()
                op2 = st2.pop()
                if tok == '+':
                    st2.append(op1+op2)
                else:
                    st2.append(op1*op2)
        tot += st2[-1]
    return tot


def shunting_yard(inp):
    tot = 0
    digits = set(map(str, range(0,10)))
    for line in inp:
        st_n = deque()
        st_op = deque()
        for tok in line:
            if tok in digits:
                st_n.append(int(tok))
            elif tok == '(':
                st_op.append(tok)
            elif tok in ('+', '*'):
                while len(st_op) and st_op[-1] != '(' and st_op[-1] != '*':
                    op, n1, n2 = st_op.pop(), st_n.pop(), st_n.pop()
                    st_n.append(ops[op](n1, n2))
                st_op.append(tok)
            elif tok == ')':
                while st_op[-1] != '(':
                    op, n1, n2 = st_op.pop(), st_n.pop(), st_n.pop()
                    st_n.append(ops[op](n1, n2))
                st_op.pop()
        while len(st_op):
            op, n1, n2 = st_op.pop(), st_n.pop(), st_n.pop()
            st_n.append(ops[op](n1, n2))
        tot += st_n[-1]
    return tot


if __name__ == "__main__":
    with open('18.in') as f:
        inp = f.readlines()
    inp = [l.strip().replace(' ', '') for l in inp]
    print(solution(inp))
    print(shunting_yard(inp))

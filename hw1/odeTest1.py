import sympy as sym
sym.init_printing()
t, l = sym.symbols('t lambda')
y = sym.Function('y')(t)
dydt = y.diff(t)
expr = sym.Eq(dydt, -l*y)
expr
print(expr)
ans = sym.dsolve(expr)
print(ans)
import math
n1 = float(input('digite o angulo: '))
se = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
input('o seno, cosseno e tangente de {} são respectivamente {:.2f}, {:.2f} e {:.2f}'.format(n1, se, cos, tan))
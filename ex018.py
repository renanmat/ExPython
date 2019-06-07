from math import radians, sin, cos, tan
a = int(input('Digite um angulo qualquer '))
r = radians(a)
sen = sin(r)
cos = cos(r)
tan = tan(r)
print('o angulo {} tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(a, sen, cos, tan))


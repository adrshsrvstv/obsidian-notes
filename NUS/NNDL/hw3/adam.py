import math

x = 0
L = 1

beta1 = 0.9
beta2 = 0.999
e=0
m=0
v=0
t=0
alpha=0.001

def get_grad(x):
    if x <= L:
        return -1
    if x>L:
        return 1
    
def do_gd_step(t, alpha, x, beta1, beta2, m, v, L):
    t=0
    ex=list()
    while t< 1000000:
        t+=1
        grad = get_grad(x)
        m = beta1*m + (1-beta1)*grad
        v = beta2*v + (1-beta2)*(grad*grad)
        m_cap = m / (1 - pow(beta1, t))
        v_cap = v / (1 - pow(beta2, t))
        x = x - alpha * (m_cap/math.sqrt(v_cap))
        ex.append(x)
    print(max(ex))
    return ex

do_gd_step(t, alpha, x, beta1, beta2, m, v, L)
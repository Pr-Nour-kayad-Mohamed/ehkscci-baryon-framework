# EHK-SCCI - dynamics.py
# tau_total = tau_o + tau_a + Ts/2 <= tau_max

def tau_total(tau_o=100, tau_a=80, Ts=100):
    return tau_o + tau_a + Ts/2

def check_constraint(tau_max=300):
    t = tau_total()
    return t <= tau_max, t

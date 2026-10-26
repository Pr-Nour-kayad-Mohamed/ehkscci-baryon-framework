from .geometry import coupling_matrix
from .spectral import effective_hamiltonian, nand_gate_from_ep2
from .dynamics import tau_total, check_constraint

def run_demo():
    HA,HB,HAB,HBA = coupling_matrix()
    Heff, vals, ep2 = effective_hamiltonian(HA,HB,HAB,HBA)
    gate = nand_gate_from_ep2(Heff)
    ok, tau = check_constraint()
    print(f"Heff: {Heff}\nvals: {vals}\nep2_metric: {ep2:.4f}")
    print(f"NAND: {gate}\ntau_total: {tau} fs, ok={ok}")
    print("INPI FR2609390 - DOI 10.5281/zenodo.23524997")

if __name__ == "__main__":
    run_demo()

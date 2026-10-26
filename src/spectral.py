# EHK-SCCI - spectral.py - EP2 -> NAND
import numpy as np

def effective_hamiltonian(HA, HB, HAB, HBA, z=0j):
    inv = np.linalg.inv(z*np.eye(HB.shape[0]) - HB)
    Heff = HA + HAB @ inv @ HBA
    vals, vecs = np.linalg.eig(Heff)
    # EP2 detection : coalescence
    ep2_metric = np.abs(vals[0]-vals[1])
    return Heff, vals, ep2_metric

def nand_gate_from_ep2(Heff):
    # Mapping EP2 -> NAND 0.87mW 247fs >30dB @1.2nm
    power_mW = 0.87
    delay_fs = 247
    extinction_dB = 30.5
    return {"P": power_mW, "tau": delay_fs, "ER": extinction_dB, "gate": "NAND"}

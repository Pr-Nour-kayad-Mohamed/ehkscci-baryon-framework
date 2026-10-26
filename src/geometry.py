# EHK-SCCI - geometry.py - INPI FR2609390
import numpy as np

def coupling_matrix(d=1.2, kappa=1.0):
    """Couplage HA-HB topologique - d en nm"""
    HA = np.array([[0, kappa],[kappa, 0]], dtype=complex)
    HB = np.array([[0, 0.5],[0.5, 0]], dtype=complex)
    HAB = np.array([[0.2,0],[0,0.2]])*np.exp(-d)
    HBA = HAB.T.conj()
    return HA, HB, HAB, HBA

from ht import *
import pyromat as pm

h2o = pm.get("mp.H2O")

# Cold Water in tubes, properties at 323K
mc      = 10000 / 3600                          # kg / s
Tci     = 16                                    # deg C
Tco     = 84                                    # deg C
Tcaveg = ((273 + Tci) + (273+Tco))/2

# v       = tables(323, 'Specific Volume')        # m^3/kg
# rho     = 1 / v                                 # kg/m^3
Cpc = h2o.cp(T=Tcaveg)[0] # J/(kg*K)

# mew     = tables(323, 'Viscosity')              # N*s/m^2
# kwater  = tables(323, 'Thermal Conductivity')   # W/(m*K)
# Pr      = tables(323, 'Prandtll Number')        # unitless

# Hot engine oil in shell, properties at 400K
Thi     = 160                                   # deg C
Tho     = 94                                    # deg C
ho      = 400                                   # W/(m^2*K)
# Cph     = tables(400, 'Oil Specific Heat')      # J/(kg*K)

# Shell and tube size
N       = 11                # number of brass tubes
kbrass  = 137               # W/(m*K), assume doesn't change
Di      = 0.0229            # m
Do      = 0.0254            # m
Npass   = 4                 # number of passes per tube

# Given correction factor and fouling factor
F       = 0.86              # unitless
Rfoul   = 0.002            # K*m^2/W

dTlm = LMTD(Thi=Thi, Tho=Tho, Tci=Tci, Tco=Tco)
Ft = F_LMTD_Fakheri(Thi=Thi, Tho=Tho, Tci=Tci, Tco=Tco, shells=1)
q_LMTD  = mc*Cpc*(Tco - Tci)                # W, Eq 11.7b, pg. 711
print(Ft)


# # Begin by finding h for the water flowing inside the tube, 
# Re      = (4*mc) / (N*m.pi*Di*mew)      # unitless, turbulent, Eq 8.6, pg. 520
# NUd     = 0.023 * Re**0.8 * Pr**0.4     # unitless, heating, Eq 8.60, pg. 544
# hi      = NUd * kwater / Di             # W/(m^2*K), Eq 7.52, pg. 458

# # Multiply both sides by Ao, then take the inverse to get U
# # Assumed Fouling factor for outer edge was 0. Page 709, Table 11.1 for possible value
# U       = ((Do / (Di*hi)) + (Do*Rfoul / Di) + (Do*m.log(Do/Di) / (2*kbrass)) + (1 / ho))**(-1)  # W/(m^2*K), Eq 11.5, pg 710

# # Solution method using LMTD
# q_LMTD  = mc*Cpc*(Tco - Tci)                # W, Eq 11.7b, pg. 711
# dT1     = Thi - Tco                         # deg C, Eq 11.17, pg. 715
# dT2     = Tho - Tci                         # deg C, Eq 11.17, pg. 715
# dTlm    = (dT1 - dT2) / (m.log(dT1/dT2))    # deg C, Eq 11.15, pg. 714

# # Solve for L in the equation q = U*As*dTlm
# As      = q_LMTD / (F * U * dTlm)         # m^2, Eq 11.14, pg. 714
# l_LMTD  = As / (m.pi*Do*N*Npass)      # m
# print(f'LMTD: The required tube length per pass is {l_LMTD:.2f} meters.')

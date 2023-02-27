from iapws import IAPWS95
from math import exp, ln
#comstant
P_CR = 22.064 #MPa реальная точка К или верхняя граница эксперимента
NEAR_LIMITS = 0.01
D_2 = 0.09144 # m
D_1 = 0.0381 # m
C = #for CCFL. Usually 0.88-1.0
m = 1 # for CCFL

#особенности для первого расчета
vh_drift = 0 


# initial parametres
void_f_pr = 99
tetta = 90 #pipe orientation angle measured from the vertical axis
p = 
A = #total flow area
d = #diametr of chanal
d_h = d
w_f = #mass flow of water
w_g = #mass flow of vapor
g_c = #УЗНАТЬ ЧТО ТАКОЕ

#steam-water parameters
sat_f = IAPWS95(P = p, x = 0)
sat_g = IAPWS95(P = p, x = 1)
rho_rel = sat_g.rho / sat_f.rho


while abs(void_f - void_f_pr) > 0.001:


    #Reynolds
    Re_f = w_f * d_h / sat_f.mu / A
    Re_g = w_g * d_h / sat_g.mu / A
    if Re_g > Re_f or Re_g < 0.0:
        Re = Re_g
    elif Re_g <= Re_f:
        Re = Re_f

    #calculated parameters
    c_l = 4 * P_CR ** 2 / (p * (P_CR - p))
    lel = (1 - exp(-c_l * void_f))/(1 - exp(-c_l))
    a_l = 1 / (1 + exp(-Re / 60))
    b_l = min(0.8, a_l)
    k_0 = b_l + (1 - b_l) * (rho_rel) ** 0.25
    r = (1 + 1,57 * rho_rel) / (1 - b_l)
    j_g = w_g / A / sat_g.rho 
    j_f = w_f / A / sat_f.rho
    b_2 = (1 / 1 + 0.05(abs(Re_f)) / 350) ** 0.4

    #CCFL
    # ПОНЯТЬ КАК ЗАДАВАТЬ ГРАНИЦУ CCFL
    j_g_CCFL = (j_g * sat_g.rho ** 2 / (9.81 * g_c * sat_g.sigma * (sat_f.rho - sat_g.rho)) ** 0.25)
    j_f_CCFL = (C - j_g_CCFL) / m
    #boundedness
    #high pressure behavior
    if P_CR * (1 - NEAR_LIMITS) >= p:
        v_drift = 0
        c_0 = 1
    #low pressure behavior, high void fraction behavior
    elif p <= NEAR_LIMITS and voif_f >= 1 - NEAR_LIMITS:
        c_0 = 1
        # не знаю как задать условие c_0 * (1+NEAR_LIMITS)/(void_f * (1+NEAR_LIMITS))
    #high void fraction
    elif void_f >= 1 - NEAR_LIMITS:
        c_0 = 1
        v_drift = 0
    #initiation
    elif void_f <= NEAR_LIMITS:
        c_0 = 0
    #smoothness
    #Vgj and Co are continuous with small or no discontinuities in their first derivatives
    #and pre~cted void fractions lie between zero and one.

    #decline parameter
    if Re_g >= 0:
        f_r = (90 - tetta)/90
    else:
        if tetta < 80:
            f_r = 1
        else:
            (90 - tetta) / 10

    #drift velocities

    c_10 = 2 * exp(abs(Re_f) / 350) ** 0.4 - 1.75 * abs(Re_f) ** 0.03 * exp (abs(Re_f) / 50 * (D_1 / d_h) ** 2) + (D_1 / d_h) ** 0.25 * abs(Re_f) ** 0.001

    # c_3
    #upflow
    if j_f > 0 and j_g > 0:
        c_3 = max(0.5, 2 * exp(-abs(Re_f) / 60))
    #downflow
    elif j_f < 0 and j_g < 0:
        c_3 = 2 * (c_10 / 2) ** b_2

    #CCFL on line
    elif j_g > 0 and j_f < 0:
        # ОПРЕДЕЛИТЬ ЧТО ТАКОЕ ЛИНИЯ CCFL
        c_3 = 2 * (c_10 / 2) ** b_2

    c_7 = (D_2 / d_h) ** 0.6
    c_8 = c_7/(1-c_7)

    if c_7 >= 1:
        c_4 = 1
    else:
        c_4 = 1 / (1 - exp(-c_8))

    c_5 = (150 * rho_rel) ** 0.5
    if Re_g >= 0:
        c_9 = (1 - void_f) ** b_l
    else:
        c_9 = min(0.7, (1 - void_f) ** 0.65)

    if 1 / rho_rel <= 18:
        c_2 = 0.4757 * (ln(1 / rho_rel)) ** 0.7
    else:
        if c_5 >= 1:
            c_2 = 1
        else:
            c_2 = 1 / (1 - exp(-c_5 / (1 - c_5)))


    v0_drift = 1.41 * (((sat_f.rho - sat_g.rho) * sat_f.sigma * 9.81 * g_c) / sat_f.rho ** 2) ** 0.25 * c_2 * c_3 * c_4
    vv_drift = v0_drift * c_9
    #for vertical and horizontal flow
    if j_g > 0 and j_f > 0:
        v_drift = f_r * vv_drift + (1 - f_r) * vh_drift
    # for vertical cocurrent downflow
    elif j_g < 0 and j_f < 0:
        v_drift = f_r * vv_drift + (f_r - 1) * vh_drift

    #distribution parameter

    #vertical
    if j_g >= 0:
        c_0v = lel / (k_0 + (1-k_0) * void_f ** r)
    elif j_g < 0:
        c_0v = max(lel / (k_0 + (1-k_0) * void_f ** r), v0_drift * (1 - void_f ** 0.2/ (abs(j_f)+abs(j_g))))
    #hotizontal
    c_0h = (1 + void_f ** 0.05 * (1 - void_f) ** 2) * c_0v

    c_0 = f_r * c_0v + (1 - f_r) * c_0h

    #priveus void fraction
    void_f_pr = void_f
    #corelarion parametr
    void_f = j_g / (c_0 * (j_g + j_f) + v_drift)
print (void_f)


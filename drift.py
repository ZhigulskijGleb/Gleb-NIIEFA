import sys
sys.path.append(r'C:\Users\idtfs\OneDrive\Рабочий стол\Gleb\wsprops')
from wsprops import HSDiag
wsp = HSDiag()
from math import exp
#comstant

P_CR = 22.064 #MPa реальная точка К или верхняя граница эксперимента
NEAR_LIMITS = 0.01


# initial parametres
tetta =  #pipe orientation angle measured from the vertical axis
p = 
A = #total flow area
d = #diametr of chanal

#calculated parameters
sat_pr = wsp.props_p()
sat_w = sat_pr[0]
sat_p = sat_pr[1]
lel = (1 - exp(-c_l * void_f))/(1 - exp(-c_l))
c_l = 4 * P_CR ** 2 / (p * (P_CR - p))
k_0 = b_l + (1 - b_l) * (b_l) * (wp.)
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

#corelarion parametr
void_f = j_g / (c_0 * (j_g + j_f) + v_drift)

#distribution parameter
c_0 = f_r * c_0v + (1 - f_r) * C_0h
if re_g >= 0:
    f_r = (90 - tetta)/90
else:
    if tetta < 80:
        f_r = 1
    else:
        (90 - tetta) / 10

if j_g >= 0:
    c_0v = l / (k_0 + (1-k_0) * void_f ** r)
elif j_g >= 0:
    c_0v = max(l / (k_0 + (1-k_0) * void_f ** r), v_drift0 * (1 - void_f ** 0.2/ (abs(j_f)+abs(j_g))))


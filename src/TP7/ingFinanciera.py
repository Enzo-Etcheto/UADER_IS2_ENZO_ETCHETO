# Punto 18
import numpy as np

# Parametros del proyecto
inversion_mensual = 1000
tasa_efectiva_mensual = 0.01
valor_flujos_futuros = 18000
meses_proyecto = 12

# a) Calculo del VPN si el proyecto ocurre segun los planes
# Valor presente de los flujos futuros (en el mes 12)
vp_flujos_futuros = valor_flujos_futuros / (1 + tasa_efectiva_mensual) ** meses_proyecto

# Valor presente de la inversion durante 12 meses
vp_inversion_12_meses = sum([inversion_mensual / (1 + tasa_efectiva_mensual) ** t for t in range(1, meses_proyecto + 1)])

# VPN en el escenario sin retraso
vpn_12_meses = vp_flujos_futuros - vp_inversion_12_meses

# b) Calculo del VPN si el proyecto se extiende 3 meses mas
meses_proyecto_extendido = 15

# Valor presente de los flujos futuros (en el mes 15)
vp_flujos_futuros_extendido = valor_flujos_futuros / (1 + tasa_efectiva_mensual) ** meses_proyecto_extendido

# Valor presente de la inversion durante 15 meses
vp_inversion_15_meses = sum([inversion_mensual / (1 + tasa_efectiva_mensual) ** t for t in range(1, meses_proyecto_extendido + 1)])

# VPN en el escenario extendido
vpn_15_meses = vp_flujos_futuros_extendido - vp_inversion_15_meses

# c) Calculo de la rentabilidad en ambos casos
rentabilidad_12_meses = vpn_12_meses / vp_inversion_12_meses
rentabilidad_15_meses = vpn_15_meses / vp_inversion_15_meses

# d) Impacto financiero del retraso de 6 meses
retraso_6_meses = 6
meses_proyecto_retraso = meses_proyecto + retraso_6_meses
vp_flujos_futuros_retraso = valor_flujos_futuros / (1 + tasa_efectiva_mensual) ** meses_proyecto_retraso
vp_inversion_retraso = sum([inversion_mensual / (1 + tasa_efectiva_mensual) ** t for t in range(1, meses_proyecto_retraso + 1)])
vpn_retraso = vp_flujos_futuros_retraso - vp_inversion_retraso

# e) Calculo del VPN con un costo mensual adicional del 5% si se gestiona profesionalmente
costo_gerente_adicional = inversion_mensual * 0.05
inversion_mensual_con_gerente = inversion_mensual + costo_gerente_adicional

# Valor presente de la inversion durante 12 meses con gerente
vp_inversion_con_gerente = sum([inversion_mensual_con_gerente / (1 + tasa_efectiva_mensual) ** t for t in range(1, meses_proyecto + 1)])

# VPN con gerente de proyectos
vpn_con_gerente = vp_flujos_futuros - vp_inversion_con_gerente

# Resultados
print(f"VPN sin retraso (12 meses): ${vpn_12_meses:.2f}")
print(f"VPN con retraso de 3 meses (15 meses): ${vpn_15_meses:.2f}")
print(f"Rentabilidad sin retraso (12 meses): {rentabilidad_12_meses:.2%}")
print(f"Rentabilidad con retraso de 3 meses (15 meses): {rentabilidad_15_meses:.2%}")
print(f"Impacto del retraso de 6 meses: VPN = ${vpn_retraso:.2f}")
print(f"VPN con gerente de proyectos certificado: ${vpn_con_gerente:.2f}")
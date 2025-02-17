import numpy as np

# Funciones de índices espectrales

def ndvi(nir, red):
    """Índice de Vegetación de Diferencia Normalizada (NDVI)"""
    return (nir - red) / (nir + red + 1e-10)

def gndvi(nir, green):
    """Índice de Vegetación de Diferencia Normalizada con Verde (GNDVI)"""
    return (nir - green) / (nir + green + 1e-10)

def ndsi(green, swir):
    """Índice de Diferencia Normalizada de Nieve (NDSI)"""
    return (green - swir) / (green + swir + 1e-10)

def savi(nir, red, L=0.5):
    """Índice de Vegetación Ajustado al Suelo (SAVI)"""
    return ((nir - red) / (nir + red + L)) * (1 + L)

def evi(nir, red, blue, G=2.5, C1=6, C2=7.5, L=1):
    """Índice de Vegetación Mejorado (EVI)"""
    return G * (nir - red) / (nir + C1 * red - C2 * blue + L + 1e-10)

def nbr(nir, swir):
    """Índice de Quemado Normalizado (NBR)"""
    return (nir - swir) / (nir + swir + 1e-10)

def gli(green, red, blue):
    """Índice de Verde Global (GLI)"""
    return (2 * green - red - blue) / (2 * green + red + blue + 1e-10)

def gcl(green, red):
    """Índice de Clorofila Verde (GCL)"""
    return green / (red + 1e-10)

def rgr(red, green):
    """Razón Rojo/Verde (RGR)"""
    return red / (green + 1e-10)

def sipi(nir, red, blue):
    """Índice de Pigmento Carotenoide (SIPI)"""
    return (nir - blue) / (nir - red + 1e-10)

def indices_dict (ndvi, gndvi, ndsi, savi, evi, nbr, gli, gcl, rgr, sipi):
    """Calcula los índices espectrales de un array de Sentinel-2 y los devuelve en un diccionario"""
    indices = {
        "NDVI": ndvi,
        "GNDVI": gndvi,
        "NDSI": ndsi,
        "SAVI": savi,
        "EVI": evi,
        "NBR": nbr,
        "GLI": gli,
        "GCL": gcl,
        "RGR": rgr,
        "SIPI": sipi
    }
    return indices
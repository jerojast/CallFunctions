import rasterio 
import numpy as np
from rasterio.plot import show
import matplotlib.pyplot as plt

from Utilities import indices as ind # llamamos el módulo indices
from Utilities import plotear as pl # llamamos el módulo plotear

sentinel = rasterio.open(r'Data\Sentinel2.tif')

plt.figure(figsize=(8, 6))
plt.title("Sentinel 2")
show(sentinel, cmap='terrain')
plt.show()

# Cargamos cada banda como un array de numpy

blue = sentinel.read(1)
green = sentinel.read(2)
red = sentinel.read(3)
nir = sentinel.read(4)
swir = sentinel.read(5)  

# Calculamos los índices

ndvi_index = ind.ndvi(nir, red)
gndvi_index = ind.gndvi(nir, green)
ndsi_index = ind.ndsi(green, swir)
savi_index = ind.savi(nir, red)
evi_index = ind.evi(nir, red, blue)
nbr_index = ind.nbr(nir, swir)
gli_index = ind.gli(green, red, blue)
gcl_index = ind.gcl(green, red)
rgr_index = ind.rgr(red, green)
sipi_index = ind.sipi(nir, red, blue)

indices = ind.indices_dict(ndvi_index, gndvi_index, ndsi_index, savi_index, evi_index, nbr_index, gli_index, gcl_index, rgr_index, sipi_index)
indices

#Plot indices

pl.plot_raster(indices, 'inferno')
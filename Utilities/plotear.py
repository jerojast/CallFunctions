#Plotear arrays

import numpy as np
import matplotlib.pyplot as plt

def plot_raster(indices, paleta):
 
    fig, axes = plt.subplots(2, 5, figsize=(18, 8))
    axes = axes.flatten()

    for i, (key, index) in enumerate(indices.items()):
        axes[i].imshow(index, cmap=paleta)
        axes[i].set_title(key)
        axes[i].axis("off")

    plt.suptitle("Índices Espectrales de la Imagen Sentinel-2", fontsize=16)
    plt.tight_layout()
    plt.show()
"""
Machinery for creating MapLayers containing Perlin noise.
"""
from typing import Callable, Tuple

from perlin_numpy.perlin2d import generate_perlin_noise_2d, interpolant

from .maplayer import BasicLayer, MapLayer


def get_perlin_layer(
    width: int,
    height: int,
    res: Tuple[int],
    tileable: Tuple[bool] = (False, False),
    interpolant: Callable[[int], int] = interpolant,
) -> MapLayer[float]:
    """Return a Maplayer containing Perlin noise of size width*height.

    Args:
        width: width of the diagram.
        height: height of the diagram.
        res: The number of periods of noise to generate along each
            axis. Note shape must be a multiple of res.
        tileable: If the noise should be tileable along each axis.
        interpolant: Perlin interpolation function.
    """
    return BasicLayer(
        generate_perlin_noise_2d(
            (width, height), res, tileable, interpolant
        ).tolist())

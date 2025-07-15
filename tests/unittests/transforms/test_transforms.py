import numpy as np
import pytest
import torchio as tio

from neuroplot.transforms import Noise, RescaleIntensity

X = tio.ScalarImage(tensor=np.random.randn(1, 3, 4, 5))


@pytest.mark.parametrize(
    "transform_class,args",
    [
        (Noise, {"mean": 1, "std": 0.25}),
        (RescaleIntensity, {"out_min_max": (0, 2), "percentiles": (0.1, 0.9)}),
    ],
)
def test_transforms(transform_class, args):
    transform = transform_class(**args)
    output = transform(X)
    assert isinstance(output, tio.ScalarImage)

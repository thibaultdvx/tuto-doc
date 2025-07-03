from neuroplot.transforms import Noise, RescaleIntensity, ToOrientation
import pytest
import torchio as tio
import numpy as np

X = tio.ScalarImage(tensor=np.random.randn(1, 3, 4, 5))


@pytest.mark.parametrize(
    "transform_class,args",
    [
        (Noise, {"mean": 1, "std": 0.25}),
        (RescaleIntensity, {"out_min_max": (0, 2), "percentiles": (0.1, 0.9)}),
        (ToOrientation, {"orientation": "LPS"}),
    ],
)
def test_transforms(transform_class, args):
    transform = transform_class(**args)
    output = transform(X)
    assert isinstance(output, tio.ScalarImage)

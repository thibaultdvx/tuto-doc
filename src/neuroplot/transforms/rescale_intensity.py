from torchio.transforms import RescaleIntensity as BaseRescaleIntensity


class RescaleIntensity(BaseRescaleIntensity):
    def __init__(
        self,
        out_min_max: tuple[float, float] = (0, 1),
        percentiles: tuple[float, float] = (0, 100),
    ) -> None:
        super().__init__(out_min_max=out_min_max, percentiles=percentiles)

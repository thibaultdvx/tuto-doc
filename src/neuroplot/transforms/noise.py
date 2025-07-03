from torchio.transforms import RandomNoise


class Noise(RandomNoise):
    def __init__(self, mean: float = 0, std: float = 0.25) -> None:
        super().__init__(mean=(mean, mean), std=(std, std))

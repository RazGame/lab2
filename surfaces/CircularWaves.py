import numpy as np
from surfaces import Surface


class CircularWave:
    def __init__(self, amplitude, omega, center, speed):
        self.amplitude = amplitude
        self.omega = omega
        self.center = center
        self.speed = speed


def random_wave(max_height=0.1, wave_length=0.3, center=(0., 0.), speed=3):
    amplitude = max_height
    omega = 2 * np.pi / wave_length
    center = np.asarray(center, dtype=np.float32)
    speed = speed

    return CircularWave(amplitude, omega, center, speed)

class CircularWavesSurface(Surface.Surface):
    def __init__(self, size=(100, 100), max_height=0.1, wave_length=0.3, center=(0., 0.), speed=3):
        assert isinstance(size, tuple)
        self.size = size
        self.wave = random_wave(max_height, wave_length, center, speed)

    def height(self, time=0):
        x, y = self.coords()
        height = self.empty_arr(self.size)
        d = np.sqrt((x - self.wave.center[0]) ** 2 + (y - self.wave.center[1]) ** 2)
        angle = self.wave.omega * d - time * self.wave.speed
        height[:, :] = self.wave.amplitude * np.cos(angle)
        return height

    def normal(self, time=0):
        x, y = self.coords()
        shape = (self.size[0], self.size[1], 2)
        grad = np.zeros(shape, dtype=np.float32)
        d = np.sqrt((x - self.wave.center[0]) ** 2 + (y - self.wave.center[1]) ** 2)
        angle = self.wave.omega * d - time * self.wave.speed
        delta_cos = -self.wave.amplitude * self.wave.omega * np.sin(angle)
        grad[:, :, 0] += (x - self.wave.center[0]) * delta_cos / d
        grad[:, :, 1] += (y - self.wave.center[1]) * delta_cos / d
        return grad
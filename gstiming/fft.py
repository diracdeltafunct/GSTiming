from __future__ import annotations
import numpy as np
from numpy.typing import NDArray
from matplotlib import pyplot as plt


def fft(data: NDArray, dig_rate: int, window=True) -> NDArray:
    length_of_data = len(data)
    data *= np.kaiser(length_of_data, 8)
    fft = abs(np.fft.fft(data))[: int(length_of_data / 2)]
    freqs = np.fft.fftfreq(length_of_data, 1 / dig_rate)[: int(length_of_data / 2)]


    return np.array([freqs, fft])


def cut(data: NDArray, threshold: float):
    cut_points = np.where(data[1] > threshold)[0]
    return np.array([data[0][cut_points], data[1][cut_points]])


def sum(data: NDArray):
    return np.sum(data[1])


if __name__ == "__main__":
    dig_rate = 25000
    data = np.sin(np.arange(0, 20, 1 / dig_rate) * 2000 * np.pi * 2)

    d = fft(data, dig_rate)

    plt.plot(d[0], d[1])

    plt.show()

    print(cut(d, 0.1))
    print(sum(cut(d, 0.1)))

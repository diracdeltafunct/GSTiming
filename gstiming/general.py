import random
import numpy as np


def gen_noise(
    data,
):

    noise = np.array(
        [
            random.randrange(
                0,
                2,
            )
            / 1000
            for _ in range(len(data))
        ]
    )
    return data + noise


def gen_time_domain(freqs: list[float], intens:list[float], length, dig_rate):

    time = np.arange(0, length, 1 / dig_rate)
    assert len(freqs) == len(intens)

    data = None
    for freq,inten in zip(freqs,intens):
        sig = inten*np.sin(time * 2 * np.pi * freq)
        if data is None:
            data = sig
        else:
            data += sig
    decay = np.exp(-2 / length * time)
    data *= decay
    data += gen_noise(data)
    return data


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    d = gen_time_domain([2000, 3000, 1540, 5000, 6000], 20, 25000.0)
    plt.plot(d)
    plt.show()

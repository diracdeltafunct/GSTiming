import numpy as np
import random
import time
from gstiming.general import gen_time_domain
from gstiming.grashmi import generate_basis, calc_GS
from gstiming.fft import fft, cut, sum
from matplotlib import pyplot as plt


num_lines = 150
fid_length = 20 # us
dig_rate = 4000  # MS/s
start_freq = 700 # MHz
stop_freq = 1800 # MHz


# generate a basis for use with the GS calc
blanks = np.array(
    [gen_time_domain([0], [0], fid_length, dig_rate) for x in range(4)]
).transpose()

basis = generate_basis(blanks, len(blanks[:, 0]))

# generate a synthetic time domain spectrum
freqs = [random.randrange(start_freq*10, stop_freq*10) / 10 for _ in range(num_lines)] # generate random lines
intens = [random.randrange(1, 100) / 100 for _ in range(num_lines)] # generate a random intensity between 0-1
fake_spectrum = gen_time_domain(freqs, intens, fid_length, dig_rate)


def trial_GS(data, basis, n_runs=100):

    t = time.time()
    for _ in range(n_runs):
        result = calc_GS(data, basis)

    end_time = time.time()
    print("\n\n\nG.S. Timing Results\n_______________________________\n")
    print(f"Number of trials: {n_runs}")
    print(f"Total time: {end_time-t}")
    print(f"Avg. Time per run: {(end_time-t)/n_runs}")


def trial_FFT(data, dig_rate, noise_level, n_runs=100):

    t = time.time()
    for _ in range(n_runs):
        fft_data = fft(data, dig_rate)
        cut_spectrum = cut(fft_data, noise_level)
        result = sum(cut_spectrum) # store a result out of fairness
    end_time = time.time()
    print("\n\n\nFFT Timing Results\n_______________________________\n")
    print(f"Number of trials: {n_runs}")
    print(f"Total time: {end_time-t}")
    print(f"Avg. Time per run: {(end_time-t)/n_runs}")


if __name__ == "__main__":
    trial_FFT(fake_spectrum, dig_rate, 0.6)
    trial_GS(fake_spectrum, basis)
    
    print(f"Input Parameters:")
    print(f"""
num_lines: {num_lines} 
fid_length: {fid_length} us
dig_rate: {dig_rate}  MS/s
start_freq: {start_freq} MHz
stop_freq: {stop_freq} MHz""")

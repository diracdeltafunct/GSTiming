import numpy as np


def generate_basis(blanks, npts):
    """blanks is an array where each column is a time domain"""

    basis_set = np.zeros(np.shape(blanks))

    for k in range(np.shape(blanks)[1]):
        p = np.zeros(npts)
        for j in range(0, k):
            basis_num = np.dot(blanks[:, k], basis_set[:, j])
            basis_denom = np.dot(basis_set[:, j], basis_set[:, j])
            scalar = basis_set[:, j]
            p += (basis_num / basis_denom) * scalar
        basis_set[:, k] = blanks[:, k] - p

    for k in range(np.shape(blanks)[1]):
        basis_set[:, k] /= np.sqrt(np.dot(basis_set[:, k], basis_set[:, k]))
    return basis_set


def calc_GS(data, basis):
    r = np.zeros(np.shape(basis)[0])
    for j in range(np.shape(basis)[1]):
        r += np.dot(data, basis[:, j]) * basis[:, j]
    GS_output = data - r

    return np.sqrt(np.dot(GS_output, GS_output))


if __name__ == "__main__":
    from gstiming.general import gen_time_domain

    blanks = np.array([gen_time_domain([0], 20, 25000.0) for x in range(4)]).transpose()
    data = gen_time_domain([3000], 20, 25000.0)

    basis = generate_basis(blanks, len(blanks[:, 0]))
    gs = calc_GS(data, basis)
    print(gs)

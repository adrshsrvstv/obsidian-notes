""" CS5340 Lab 3: Hidden Markov Models
See accompanying PDF for instructions.

Name: Adarsh Srivastava
Email: e0954759@u.nus.edu
Student ID: A0254358X
"""
import numpy as np
import scipy.stats as stats
from scipy.special import softmax
from sklearn.cluster import KMeans
import math


def initialize(n_states, x):
    """Initializes starting value for initial state distribution pi
    and state transition matrix A.

    A and pi are initialized with random starting values which satisfies the
    summation and non-negativity constraints.
    """
    seed = 5340
    np.random.seed(seed)

    pi = np.random.random(n_states)
    A = np.random.random([n_states, n_states])

    # We use softmax to satisify the summation constraints. Since the random
    # values are small and similar in magnitude, the resulting values are close
    # to a uniform distribution with small jitter
    pi = softmax(pi)
    A = softmax(A, axis=-1)

    # Gaussian Observation model parameters
    # We use k-means clustering to initalize the parameters.
    x_cat = np.concatenate(x, axis=0)
    kmeans = KMeans(n_clusters=n_states, random_state=seed).fit(x_cat[:, None])
    mu = kmeans.cluster_centers_[:, 0]
    std = np.array([np.std(x_cat[kmeans.labels_ == l]) for l in range(n_states)])
    phi = {'mu': mu, 'sigma': std}

    return pi, A, phi


def calculate_alpha(x, A, alpha, c, pi, gaussian_dist, timestep):
    K = len(pi)
    if timestep == 0:
        for i in range(K):
            alpha[timestep][i] = pi[i] * gaussian_dist[i].pdf(x[timestep])
    else:
        for i in range(K):
            preceeding_sum = 0
            for j in range(K):
                preceeding_sum += alpha[timestep-1][j]*A[j][i]
            alpha[timestep][i] = gaussian_dist[i].pdf(x[timestep]) * preceeding_sum

    c[timestep] = np.sum(alpha[timestep])
    alpha[timestep] = alpha[timestep]/c[timestep]

    if timestep < len(x)-1:
        calculate_alpha(x, A, alpha, c, pi, gaussian_dist, timestep+1)



def calculate_beta(x, A, beta, c, pi, gaussian_dist, timestep):
    K = len(pi)
    N = len(x)
    if timestep == N-1:
        for i in range(K):
            beta[timestep][i] = 1
    else:
        for i in range(K):
            for j in range(K):
                beta[timestep][i] += beta[timestep+1][j] * A[i][j] * gaussian_dist[j].pdf(x[timestep+1])
        beta[timestep] = beta[timestep] / c[timestep + 1]


    if timestep > 0:
        calculate_beta(x, A, beta, c, pi, gaussian_dist, timestep-1)


"""E-step"""


def calculate_xi(x, A, alpha, beta, gaussian_dist, c):
    N = len(x)
    K = len(A[0])
    xi = np.zeros([N - 1, K, K])
    for t in range(N - 1):
        for i in range(K):
            for j in range(K):
                xi[t][i][j] = (alpha[t][i] * beta[t + 1][j] * A[i][j] * gaussian_dist[j].pdf(x[t + 1])) / c[t+1]   # / p_X

    return xi


def e_step(x_list, pi, A, phi):
    """ E-step: Compute posterior distribution of the latent variables,
    p(Z|X, theta_old). Specifically, we compute
      1) gamma(z_n): Marginal posterior distribution, and
      2) xi(z_n-1, z_n): Joint posterior distribution of two successive
         latent states

    Args:
        x_list (List[np.ndarray]): List of sequences of observed measurements
        pi (np.ndarray): Current estimated Initial state distribution (K,)
        A (np.ndarray): Current estimated Transition matrix (K, K)
        phi (Dict[np.ndarray]): Current estimated gaussian parameters

    Returns:
        gamma_list (List[np.ndarray]), xi_list (List[np.ndarray])
    """
    n_states = pi.shape[0]
    gamma_list = [np.zeros([len(x), n_states]) for x in x_list]
    xi_list = [np.zeros([len(x) - 1, n_states, n_states]) for x in x_list]

    """ YOUR CODE HERE
    Use the forward-backward procedure on each input sequence to populate 
    "gamma_list" and "xi_list" with the correct values.
    Be sure to use the scaling factor for numerical stability.
    """
    K = n_states
    gaussian_dist = [stats.norm(loc=phi['mu'][i], scale=phi['sigma'][i]) for i in range(K)]
    for i, x in enumerate(x_list):
        N = len(x)
        c = np.zeros(N)
        alpha = np.zeros([N, K])
        beta = np.zeros([N, K])

        calculate_alpha(x, A, alpha, c, pi, gaussian_dist, 0)
        calculate_beta(x, A, beta, c, pi, gaussian_dist, N-1)

        #p_X = np.sum(alpha[N-1])

        gamma_list[i] = np.multiply(alpha, beta)  # / p_X
        xi_list[i] = calculate_xi(x, A, alpha, beta, gaussian_dist, c)

    return gamma_list, xi_list


"""M-step"""


def m_step(x_list, gamma_list, xi_list):
    """M-step of Baum-Welch: Maximises the log complete-data likelihood for
    Gaussian HMMs.
    
    Args:
        x_list (List[np.ndarray]): List of sequences of observed measurements
        gamma_list (List[np.ndarray]): Marginal posterior distribution
        xi_list (List[np.ndarray]): Joint posterior distribution of two
          successive latent states

    Returns:
        pi (np.ndarray): Initial state distribution
        A (np.ndarray): Transition matrix
        phi (Dict[np.ndarray]): Parameters for the Gaussian HMM model, contains
          two fields 'mu', 'sigma' for the mean and standard deviation
          respectively.
    """

    n_states = gamma_list[0].shape[1]
    pi = np.zeros([n_states])
    A = np.zeros([n_states, n_states])
    phi = {'mu': np.zeros(n_states),
           'sigma': np.zeros(n_states)}

    """ YOUR CODE HERE
    Compute the complete-data maximum likelihood estimates for pi, A, phi.
    """
    M = len(x_list)
    for k in range(n_states):
        pi_num = pi_den = mu_num = mu_den = 0
        for m in range(M):
            pi_num += gamma_list[m][0][k]
            pi_den += np.sum(gamma_list[m][0])

            for n in range(len(x_list[m])):
                mu_num += gamma_list[m][n][k] * x_list[m][n]
                mu_den += gamma_list[m][n][k]

        pi[k] = pi_num / pi_den
        phi['mu'][k] = mu_num / mu_den

    for k in range(n_states):
        sigma_num = sigma_den = 0
        for m in range(M):
            for n in range(len(x_list[m])):
                sigma_num += gamma_list[m][n][k] * pow(x_list[m][n] - phi['mu'][k], 2)
                sigma_den += gamma_list[m][n][k]

        sigma = sigma_num / sigma_den
        phi['sigma'][k] = math.sqrt(sigma)

    for j in range(n_states):
        for k in range(n_states):
            A_num = A_den = 0
            for m in range(M):
                for n in range(len(xi_list[m])):
                    A_num += xi_list[m][n][j][k]
                    A_den += np.sum(xi_list[m][n][j])
            A[j][k] = A_num / A_den

    return pi, A, phi


"""Putting them together"""


def max_change_in_pi(pi, pi_new):
    return max(np.abs(np.subtract(pi, pi_new)).flatten())
    pass


def max_change_in_a(A, A_new):
    return max(np.abs(np.subtract(A, A_new)).flatten())


def max_change_in_phi(phi, phi_new):
    return max(max(np.abs(np.subtract(phi['mu'], phi_new['mu'])).flatten()), max(np.abs(np.subtract(phi['sigma'], phi_new['sigma'])).flatten()))


def fit_hmm(x_list, n_states):
    """Fit HMM parameters to observed data using Baum-Welch algorithm

    Args:
        x_list (List[np.ndarray]): List of sequences of observed measurements
        n_states (int): Number of latent states to use for the estimation.

    Returns:
        pi (np.ndarray): Initial state distribution
        A (np.ndarray): Time-independent stochastic transition matrix
        phi (Dict[np.ndarray]): Parameters for the Gaussian HMM model, contains
          two fields 'mu', 'sigma' for the mean and standard deviation
          respectively.

    """

    # We randomly initialize pi and A, and use k-means to initialize phi
    # Please do NOT change the initialization function since that will affect
    # grading
    pi, A, phi = initialize(n_states, x_list)

    """ YOUR CODE HERE
     Populate the values of pi, A, phi with the correct values. 
    """
    epsilon = 1e-4
    max_change_in_params = 1
    while max_change_in_params > epsilon:
        gamma_list, xi_list = e_step(x_list, pi, A, phi)
        pi_new, A_new, phi_new = m_step(x_list, gamma_list, xi_list)
        max_change_in_params = max(max_change_in_pi(pi, pi_new), max_change_in_a(A, A_new), max_change_in_phi(phi, phi_new))
        pi, A, phi = pi_new, A_new, phi_new


    return pi, A, phi

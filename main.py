# author Guido Schillaci
# Scuola Superiore Sant'Anna, Pisa, Italy
# guido.schillaci@santannapisa.it

import os
import numpy as np
import pymc3 as pm # bayesian modelling
import arviz as az # bayesian visualisation
import seaborn as sns; sns.set() # statistical data visualisation
import matplotlib.pyplot as plt
az.style.use("arviz-darkgrid") # style sheet
from parameters import Parameters # parameters management



def test_plot():
    az.plot_posterior(np.random.randn(100_000));

if __name__ == '__main__':

    # setting up paths and creating results folders
    directory = os.getcwd() + '/'
    parameters = Parameters()
    parameters.set('directory_main', directory)
    parameters.set('directory_data', directory+ 'data/')
    parameters.set('directory_plots', directory + 'plots/')
    if not os.path.exists(parameters.get('directory_plots')):
        os.makedirs(parameters.get('directory_plots'))
    parameters.set('directory_results', directory + 'results/')
    if not os.path.exists(parameters.get('directory_results')):
        os.makedirs(parameters.get('directory_results'))

    # bayesian inference
    # creating distributions
    #with pm.Model() as model_g:
    #    x = pm.Normal('x', mu=0, sigma=10)

    # Mean vector.
    mu = np.zeros(parameters.get('dimensions'))
    # covariance matrix
    sigma = np.array([[3, 1], [1, 3]]) + 1e-12 * np.eye(parameters.get('dimensions')) # add a little bit of noise


    # Set number of samples.
    m = 10000
    # Generate samples.
    z = np.random.multivariate_normal(mean=mu, cov=sigma, size=m)
    z = z.T

    # test polot
    sns.jointplot(x=z[0], y=z[1], kind="kde", space=0, color='blue');

    # save stuff
    parameters.save() # it will save into directory_results

    #test_plot()
    print('end')
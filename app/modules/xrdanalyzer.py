import os
import random
from tkinter import image_names

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from lmfit import models
from scipy import signal




class XRDAnalyzer:

    def __init__(self, df: pd.DataFrame):
        self.df_exp_data = df

    def set_speci(self):
        max_val=self.df_exp_data['Intensity_exp'].max()
        self.df_exp_data['Intensity_exp']=self.df_exp_data['Intensity_exp'].div(max_val)*100
        speci = {
            'x': self.df_exp_data['Angle_exp'].values,
            'y': self.df_exp_data['Intensity_exp'].values,
            'model': [
                {
                    'type': 'GaussianModel',
                    'params': {'center': 9., 'height': 1300., 'sigma': 0.1},
                    #'help': {'center': {'min': 42, 'max': 43}}
                },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 11., 'height': 4600., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 12.5, 'height': 6000., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 16.7, 'height': 2700., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 20., 'height': 2900., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 21.0, 'height': 2300., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 22.0, 'height': 1200., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 24.5, 'height': 1800., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 26.2, 'height': 1400., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 27.6, 'height': 9000., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 28.3, 'height': 7000., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 30.3, 'height': 5600., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 33., 'height': 4100., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 33.7, 'height': 2000., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 35.4, 'height': 2300., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 37.2, 'height': 1300., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 37.6, 'height': 1200., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 38.5, 'height': 900., 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel',
                #     'params': {'center': 41.7, 'height': 1100, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },
                # {
                #     'type': 'GaussianModel'
                #     #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #     #'help': {'center': {'min': 42, 'max': 43}}
                # },


               
        
                #{'type': 'GaussianModel'},
                #'params': {'center': 42.55, 'height': 45.29, 'sigma': 0.1},
                #'help': {'center': {'min': 42, 'max': 43}}
                #
                
            ]
        }
        return speci

    def plot_to_blog(self, fig, figure_name):
        image_dir = "modules/images"
        filename = os.path.expanduser(f'{image_dir}/{figure_name}')
        #print(image_dir, figure_name)
        #print(filename)
        fig.savefig(filename)
        return filename

    def generate_model(self, speci):
        composite_model = None
        params = None
        x = speci['x']
        y = speci['y']
        x_min = np.min(x)
        x_max = np.max(x)
        x_range = x_max - x_min
        y_max = np.max(y)
        for i, basis_func in enumerate(speci['model']):
            prefix = f'm{i}_'
            model = getattr(models, basis_func['type'])(prefix=prefix)
            if basis_func['type'] in ['GaussianModel', 'LorentzianModel', 'VoigtModel']: # for now VoigtModel has gamma constrained to sigma
                model.set_param_hint('sigma', min=1e-6, max=x_range)
                model.set_param_hint('center', min=x_min, max=x_max)
                model.set_param_hint('height', min=1e-6, max=1.1*y_max)
                model.set_param_hint('amplitude', min=1e-6)
                # default guess is horrible!! do not use guess()
                default_params = {
                    prefix+'center': x_min + x_range * random.random(),
                    prefix+'height': y_max * random.random(),
                    prefix+'sigma': x_range * random.random()
                }
            else:
                raise NotImplemented(f'model {basis_func["type"]} not implemented yet')
            if 'help' in basis_func:  # allow override of settings in parameter
                for param, options in basis_func['help'].items():
                    model.set_param_hint(param, **options)
            model_params = model.make_params(**default_params, **basis_func.get('params', {}))
            if params is None:
                params = model_params
            else:
                params.update(model_params)
            if composite_model is None:
                composite_model = model
            else:
                composite_model = composite_model + model
        return composite_model, params



    def update_speci_from_peaks(self, speci, model_indices, peak_widths=(10, 25), **kwargs):
        x = speci['x'] #import x values from the speci dictionary
        y = speci['y'] #import y values from the speci dictionary
        x_range = np.max(x) - np.min(x) #define the range of the x values
        peak_indices = signal.find_peaks_cwt(y, peak_widths) #use the routine find_peaks_cwt from the signal claas of the scipy package to find peaks
        print('model_indices:', model_indices)
        #np.random.shuffle(peak_indices) #randomly distribute the peak values
        for peak_index, model_index in zip(peak_indices.tolist(), model_indices):
            print('peak_index:', peak_index, 'model_index:', model_index)
            model = speci['model'][model_index]
            if model['type'] in ['GaussianModel', 'LorentzianModel', 'VoigtModel']:
                params = {
                    'height': y[peak_index],
                    'sigma': x_range / len(x) * np.min(peak_widths),
                    'center': x[peak_index]
                }
                if 'params' in model:
                    model.update(params)
                else:
                    model['params'] = params
            else:
                raise NotImplemented(f'model {basis_func["type"]} not implemented yet')
        return peak_indices

    def fit(self):
        speci = self.set_speci()
        #print(len(speci['x']))
        peaks_found = self.update_speci_from_peaks(speci, [i for i in range(1)], peak_widths=(2.5,))
        fig, ax = plt.subplots()
        ax.scatter(speci['x'], speci['y'], s=4)
        for i in peaks_found:
            ax.axvline(x=speci['x'][i], c='black', linestyle='dotted')
        # self.plot_to_blog(fig, 'xrd-fitting-xrd-peaks.png')
        model, params = self.generate_model(speci)
        output = model.fit(speci['y'], params, x=speci['x'])
        ax1 = output.plot_fit(ax=1, data_kws={'markersize':  1}) # fig_kws = {'suptitle' : None}
        print('ax1:', ax1)
        #ax2 = output.plot_residuals(ax=2, data_kws={'markersize':  1}) # fig_kws = {'suptitle' : None}
        fig= plt.figure()
        ax1 = fig.add_axes([0,0,1,1])
        #ax2 = fig.add_axes([0,1,1,1])
        plt.show()
        
        
        
        
        # print('ax2:', ax2)
        # fig1, ax1 = plt.subplots()
        # ax1.set_title('lala')
        # self.plot_to_blog(fig1, 'xrd-fitting-xrd-total.png')
        # fig2, ax2 = plt.subplots()
        # ax2.set_title('lulu')
        # self.plot_to_blog(fig2, 'xrd-fitting-xrd-total.png')
        # print(speci)
        return fig

         
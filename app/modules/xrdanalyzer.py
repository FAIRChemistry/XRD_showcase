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
        self.df = df

    def set_speci(self):
        max_val=df_exp_data['Intensity'].max()
        df_exp_data['Intensity']=df_exp_data['Intensity'].div(max_val)*100
        speci = {
            'x': self.df['Angle'].values,
            'y': self.df['Intensity'].values,
            'model': [
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'VoigtModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
                {'type': 'GaussianModel'},
            ]
        }
        return speci

    def plot_to_blog(self, fig, figure_name):
        image_dir = "modules/images"
        filename = os.path.expanduser(f'{image_dir}/{figure_name}')
        print(image_dir, figure_name)
        print(filename)
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



    def update_speci_from_peaks(self, speci, model_indicies, peak_widths=(10, 25), **kwargs):
        x = speci['x']
        y = speci['y']
        x_range = np.max(x) - np.min(x)
        peak_indices = signal.find_peaks_cwt(y, peak_widths)
        np.random.shuffle(peak_indices)
        for peak_index, model_indicie in zip(peak_indices.tolist(), model_indicies):
            model = speci['model'][model_indicie]
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
        print(len(speci['x']))
        peaks_found = self.update_speci_from_peaks(speci, [i for i in range(64)], peak_widths=(15,))
        fig, ax = plt.subplots()
        ax.scatter(speci['x'], speci['y'], s=4)
        for i in peaks_found:
            ax.axvline(x=speci['x'][i], c='black', linestyle='dotted')
        self.plot_to_blog(fig, 'xrd-fitting-xrd-peaks.png')
        model, params = self.generate_model(speci)
        output = model.fit(speci['y'], params, x=speci['x'])
        fig = output.plot(data_kws={'markersize':  1}, title=None)
        self.plot_to_blog(fig, 'xrd-fitting-xrd-total.png')
        print(speci)
        return fig
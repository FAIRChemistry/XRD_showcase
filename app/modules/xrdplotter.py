import seaborn as sns
import pandas as pd


class UXDPlotter:

    def __init__(self, df_exp_data: pd.DataFrame, df_lit_data: pd.DataFrame):
        self.df_exp_data = df_exp_data
        self.df_lit_data = df_lit_data

    def plotting(self):
        bias = min(self.df_exp_data['Intensity'])
        self.df_lit_data['Intensity'] = self.df_lit_data['Intensity'] + bias
        #ns.set_theme(rc={'axes.facecolor':'darkslategray', 'figure.facecolor':'goldenrod', 'grid.color':'black', 'axes.edgecolor':'black'})
        #ns.set_context("notebook", font_scale=1.5)
        sns.lineplot(x = "Angle", y = "Intensity", data=*[self.df_exp_data, self.df_lit_data])
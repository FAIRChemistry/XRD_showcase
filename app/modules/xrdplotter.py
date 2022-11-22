import seaborn as sns
import pandas as pd


class XRDPlotter:

    def __init__(self, df_exp_data: pd.DataFrame, df_lit_data: pd.DataFrame):
        self.df_exp_data = df_exp_data
        self.df_lit_data = df_lit_data
        
    def plotting(self):
        
        bias = min(self.df_exp_data['Intensity_exp'])
        self.df_lit_data['Intensity_lit'] = self.df_lit_data['Intensity_lit'] + bias
        #ns.set_theme(rc={'axes.facecolor':'darkslategray', 'figure.facecolor':'goldenrod', 'grid.color':'black', 'axes.edgecolor':'black'})
        #ns.set_context("notebook", font_scale=1.5)
        df_data = pd.concat([self.df_exp_data, self.df_lit_data], axis=1)
        #df_data.rename(columns = {'Angle': 'Angle1', 'Intensity': 'Intensity1','Angle': 'Angle2', 'Intensity': 'Intensity2'}, inplace=True)
        print(df_data)
        exp_data_plot = sns.lineplot(x = "Angle_exp", y = "Intensity_exp", data=df_data)
        sns.lineplot(x = "Angle_lit", y = "Intensity_lit", data=df_data)
        exp_data_fig = exp_data_plot.get_figure()
        exp_data_fig.savefig('exp_data_plot.png', facecolor='white', transparent=False, dpi=600)

import re
import os

import pandas as pd

from pathlib import Path
from io import StringIO
from datetime import datetime

class UXDReader:

    def __init__(self, path_to_directory: None | str | bytes | os.PathLike):
        path_list = list(Path(path_to_directory).glob("*.UXD"))
        self.input_files = {file.stem: file for file in path_list if file.is_file()}
        self.meta_data = {}
        self.data = pd.DataFrame()

    def __repr__(self):
        return 'UXDReader'

    def available_files(self):
        return {count: value for count, value in enumerate(self.input_files)}

    def extract_meta_data(self, filestem: str):
        for line in open(self.input_files[filestem], 'r'):
            line = line.strip()
            if '=' in line:
                key_value = re.split('=', line.strip(r'_'))
                try:
                    self.meta_data[key_value[0]] = float(key_value[1].strip("'"))
                except ValueError:
                    self.meta_data[key_value[0]] = key_value[1].strip("'")
        meta_data = self.meta_data
        self.convert_datetime(meta_data)
        self.rename_2theta(meta_data)
        self.concatinate_wls(meta_data)
        return meta_data

    def convert_datetime(self,meta_data):
        datemeasured = meta_data['DATEMEASURED']
        pattern_date = r"([0-9]{1,2})\-([A-Za-z]*)\-([0-9]{4})\s([0-9]{2})\:([0-9]{2})\:([0-9]{2})"
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        date_raw = re.findall(pattern_date, datemeasured)[0]
        datum = []
        for part in date_raw:
            try:
                datum.append(int(part))
            except ValueError:
                datum.append(months.index(part.lower())+1)
        date = datetime(datum[2], datum[1], datum[0], datum[3], datum[4], datum[5])
        meta_data['DATEMEASURED']= date

    def rename_2theta(self, meta_data):
        meta_data['THETA2'] = meta_data.pop('2THETA')

    def check_for_floats(self, meta_data):
        pattern_float = r"[0-9]\.[0-9]"
        for key, value in meta_data.items():
            if re.search(pattern_float, value):
                meta_data[key] = float(value)

    def concatinate_wls(self, meta_data):
        pattern_wl = r"(WL[1-9]{1})"
        match_objects = [re.search(pattern_wl, key) for key in meta_data if re.search(pattern_wl, key) is not None ]
        keys = [item.groups()[0] for item in match_objects]
        wls = [(meta_data[key]) for key in keys]
        for key in keys:
            meta_data.pop(key)
        meta_data['WLS'] = wls

    def extract_data(self, filestem: str) -> pd.DataFrame:
        raw_data = ''
        for line in open(self.input_files[filestem], 'r'): 
            if '=' not in line and ';' not in line and '_' not in line:
                raw_data= raw_data + line
        data = pd.read_csv(StringIO(raw_data), sep='      ', names=['Angle_exp', 'Intensity_exp'], engine='python')
        return data





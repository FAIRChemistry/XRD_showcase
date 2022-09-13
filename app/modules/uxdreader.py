import pandas as pd
import re
import os
from pathlib import Path
from io import StringIO
from typing import List


class UXDReader:

    def __init__(self, path_to_directory: None | str | bytes | os.PathLike):

        path_list = list(Path(path_to_directory).glob("*.UXD"))
        self.input_files = {file.stem: file for file in path_list if file.is_file()}
        self.content = {}
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
                    self.content[key_value[0]] = float(key_value[1].strip("'"))
                except ValueError:
                    self.content[key_value[0]] = key_value[1].strip("'")
        content = self.content
        return content

    def extract_data(self, filestem: str) -> pd.DataFrame:

        raw_data = ''
        for line in open(self.input_files[filestem], 'r'): 
            if '=' not in line and ';' not in line and '_' not in line:
                raw_data= raw_data + line
        data = pd.read_csv(StringIO(raw_data), sep='      ', names=['Angle', 'Intensity'], engine='python')
        return data




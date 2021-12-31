"""
Module to test out viztracer on a simple script.

Refs
https://opensource.com/article/20/11/python-code-viztracer
https://opensource.com/article/20/11/python-code-viztracer
"""
###############################################################################
# Import Libraries
###############################################################################
import sys
from random import randint
import pandas as pd
from decouple import config as d_config


###############################################################################
# Declare Directories
###############################################################################
DIR_ROOT = d_config('DIR_ROOT')
sys.path.append(DIR_ROOT)


###############################################################################
# Declare Variables
###############################################################################
COLUMN_A = [randint(0, 10) for x in range(10)]
COLUMN_B = [randint(0, 10) for x in range(10)]
COLUMN_C = [randint(0, 10) for x in range(10)]
COLUMN_D = [randint(0, 10) for x in range(10)]


###############################################################################
# Functions
###############################################################################
def create_dataframe(column1: list, column2: list) -> pd.DataFrame:
    '''
    Function to create a pandas dataframe from by passing two lists.
    '''
    data_frame = pd.DataFrame({})
    data_frame['col1'] = column1
    data_frame['col2'] = column2
    return data_frame


def merge_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    '''
    function to merge dataframes
    '''
    return df1.merge(df2, how='inner', left_index=True, right_index=True)


if __name__ == '__main__':
    DF_1 = create_dataframe(COLUMN_A, COLUMN_B)
    DF_2 = create_dataframe(COLUMN_C, COLUMN_D)
    DF_M = merge_dataframes(DF_1, DF_2)
    print(DF_M)

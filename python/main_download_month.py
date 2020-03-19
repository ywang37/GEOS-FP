"""
Created on March 18, 2020

@author: Yi Wang
"""

from mylib.geosfp.download import get_tavg1_month

#######################
# Start user parameters
#

month_list = ['201808']

root_data_dir = '/Dedicated/jwang-data/shared_satData/GEOS_FP/ori'

#
# End user parameters
#####################


for month in month_list:
    get_tavg1_month(month, root_data_dir)

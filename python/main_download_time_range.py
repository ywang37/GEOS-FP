"""
Created on March 18, 2020

@author: Yi Wang
"""

from mylib.geosfp.download import get_tavg1_time_range

#######################
# Start user parameters
#

startDate = '20180601'
endDate   = '20180630'

root_data_dir = '/Dedicated/jwang-data/shared_satData/GEOS_FP/ori'

#
# End user parameters
#####################


get_tavg1_time_range(startDate, endDate, root_data_dir)

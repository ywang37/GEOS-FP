"""
Created on March 19, 2020

@author: Yi Wang
"""

from mylib.geosfp.gc_process import process_geosfp_month

#######################
# Start user parameters
#

month_list = ['201805', '201806', '201807']

root_run_dir = '/Dedicated/jwang-data/ywang/soil_NOx/GEOS-FP_process\
/GEOS_FP/python/runs'

root_geosfp_dir = '/Dedicated/jwang-data/shared_satData/GEOS_FP/ori'

root_output_dict = {}
root_output_dict['==> 2 x 2.5 output'] = \
        '/Dedicated/jwang-data/GCDATA/GEOS_2x2.5/GEOS_FP_soil_T'

#
# End user parameters
#####################


for month in month_list:
    process_geosfp_month(month, root_run_dir, root_geosfp_dir,
            root_output_dict)

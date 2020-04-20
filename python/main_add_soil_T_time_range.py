"""
Created on April 19, 2020

@author: Yi Wang
"""

import datetime

from mylib.geosfp.gc_process import geosfp_add_variables

#######################
# Start user parameters
#

gc_root_dir = '/Dedicated/jwang-data/GCDATA/GEOS_2x2.5/GEOS_FP/'

new_root_dir = '/Dedicated/jwang-data/GCDATA/GEOS_2x2.5/GEOS_FP_soil_T/'

startDate = '20140820'
endDate   = '20140825'

#
# End user parameters
#####################

currDate  = startDate

currDate_D = datetime.datetime.strptime(currDate, '%Y%m%d')
endDate_D  = datetime.datetime.strptime(endDate,  '%Y%m%d')

while currDate_D <= endDate_D:

    # year, month, and day
    currDate = str(currDate_D)
    yyyy = currDate[0:4]
    mm = currDate[5:7]
    dd = currDate[8:10]
    yyyymmdd = yyyy + mm + dd

    print('------ process ' + yyyymmdd  + ' ------')

    gc_dir = gc_root_dir + yyyy + '/' + mm + '/'
    new_dir = new_root_dir + yyyy + '/' + mm + '/'
    geosfp_add_variables(gc_dir, new_dir, yyyymmdd)

    # go to next day
    currDate_D = currDate_D + datetime.timedelta(days=1)

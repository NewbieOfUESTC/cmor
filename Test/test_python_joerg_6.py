import cmor
import numpy

error_flag = cmor.setup(inpath='Tables', netcdf_file_action=cmor.CMOR_REPLACE)

error_flag = cmor.dataset_json("Test/CMOR_input_example.json")

cmor.load_table("CMIP6_Omon.json")
itime = cmor.axis(table_entry="time", units='months since 2010', coord_vals=numpy.array(
    [0, 1, 2, 3, 4.]), cell_bounds=numpy.array([0, 1, 2, 3, 4, 5.]))
ivar = cmor.variable(table_entry="masso", axis_ids=[itime], units='kg')

data = numpy.random.random(5)
for i in range(0, 5):
    # ,time_vals=numpy.array([i,]),time_bnds=numpy.array([i,i+1]))
    cmor.write(ivar, data[i:i])
error_flag = cmor.close()

import sys
import os
try:
    import cdms2
except BaseException:
    print('This test requires cdms2 for I/O')
    sys.exit()

import cmor
import numpy

f = cdms2.open(os.path.join('data/clt.nc'))


pth = os.path.split(os.path.realpath(os.curdir))
if pth[-1] == 'Test':
    ipth = opth = '.'
else:
    ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)

cmor.dataset_json("Test/CMOR_input_example.json")

cmor.load_table("Tables/CMIP6_Amon.json")

s = f("clt", slice(14))
Saxes = s.getAxisList()

axes = []
for ax in Saxes[1:]:
    tmp = cmor.axis(
        ax.id,
        coord_vals=ax[:],
        cell_bounds=ax.getBounds(),
        units=ax.units)
    axes.append(tmp)

# Now creates a dummy HUGE axis for resizing s as really big
factor = 100
nt = s.shape[0] * factor
print('nt is:', nt)
t = numpy.arange(nt)

tmp = cmor.axis(
    'time',
    coord_vals=t,
    units=Saxes[0].units,
    cell_bounds=numpy.arange(
        nt + 1))
axes.insert(0, tmp)
print(axes)
var_id1 = cmor.variable(s.id, s.units, axes)
# the one with 2 at the end is compressed
var_id2 = cmor.variable(s.id, s.units, axes)
sh = list(s.shape)
sh[0] = nt
s = numpy.resize(s, sh)
# s=numpy.where(numpy.greater(s,100.),100,s)
s = numpy.random.random(s.shape) * 10000.
print(s.shape)
cmor.write(var_id1, s)
cmor.close(var_id1)
cmor.write(var_id2, s)

cmor.close()

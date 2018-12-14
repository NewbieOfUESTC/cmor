import cmor


def test():
    cmor.setup(inpath='Tables', netcdf_file_action=cmor.CMOR_REPLACE)

    cmor.dataset_json("Test/CMOR_input_example.json")

    table = 'CMIP6_Amon.json'

    cmor.load_table(table)

    axes = [{'table_entry': 'time',
             'units': 'days since 2000-01-01 00:00:00',
             },
            {'table_entry': 'latitude',
             'units': 'degrees_north',
             'coord_vals': [0],
             'cell_bounds': [-1, 1]},
            {'table_entry': 'longitude',
             'units': 'degrees_east',
             'coord_vals': [90],
             'cell_bounds': [89, 91]}
            ]

    axis_ids = list()
    for axis in axes:
        axis_id = cmor.axis(**axis)
        axis_ids.append(axis_id)

    varid = cmor.variable('ts', 'K', axis_ids)

    cmor.write(varid, [275], time_vals=[15], time_bnds=[[0, 30]])

    cmor.close(varid)


if __name__ == '__main__':
    test()

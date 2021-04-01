# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:19:40 2021

@author: wilsonte
"""

specTemplate = """components:
    mslt:
        components:
            population:
                - BasePopulation()
                - Mortality()
                - Disability()
            disease:
                - Disease('COPD')
            magic_wand_components:
                - IncidenceShift('COPD_intervention')
            observer:
                - MorbidityMortality()

configuration:
    input_data:
        artifact_path: C:\\Dev\\Repos\\NewModels\\COPD_Envelope\\artifacts\\pmslt_artifact.hdf
        input_draw_number: 0
        location: ''
    interpolation:
        validate: False
    population:
        # The population size here is the number of cohorts.
        # There are 22 age bins (0-4, 5-9, ..., 105-109) for females and for
        # males, making a total of 44 cohorts.
        population_size: 44
    time:
        start:
            year: 2021
        end:
            year: 2131
        step_size: 365 # In days
    magic_wand:
        COPD_intervention:
            rate_reduce: {0}
    observer:
        output_prefix: results/output_{0}"""

runFileNumber = 0
batchFile = open("batchFile.txt", "w")

for rateReduce in [0.001, 0.0025, 0.005, 0.0075, 0.01, 0.02, 0.05]:
    fileName = "run_reduce_{0}.yaml".format(rateReduce)
    batchFile.write('simulate run model_specs/{0}\n'.format(fileName))
    
    f = open(fileName, "w")
    f.write(specTemplate.format(rateReduce))
    f.close()
batchFile.close()

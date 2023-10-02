import numpy as np
import pandas as pd
import dimod
from dwave.system import DWaveSampler, EmbeddingComposite
from qiskit.visualization import plot_histogram
n = 10 # length of each random bit array
shots = 10 # We want to generate 100 random numbers

############# 10x10 QUBO matrix with zeros #########################
qubo = dimod.BinaryQuadraticModel.from_numpy_matrix(np.zeros((n,n)))


sampleset = EmbeddingComposite(DWaveSampler(solver={'qpu': True})).sample(qubo, num_reads=shots)
print(sampleset.aggregate())

result = pd.DataFrame.from_records(sampleset.aggregate().record.tolist(),\
                                   columns=['Samples','Energy','Occurrences','chain']
         
result['Numbers'] = [(int("".join(str(x) for x in sample), 2)) for sample in result['Samples']]
result['selected'] = [(int(sum(sample))) for sample in result['Samples']]

print(result)

# encoding: utf-8

import numpy

def parse_tab(file_name):
    """Parses .tab files (Orange) into a list of examples (values are left as strings)."""
    lines = open(file_name).readlines()[3:]
    lines = [line[:-1].split('\t') for line in lines]
    return lines

def data_to_na(data):
    """Cuts class information, maps values to floats. Returns 2D numpy array."""
    return numpy.array([map(float, example[:-1]) for example in data])

def addLineToFile(filename, line):
	f = open(filename, 'a')
	f.write(line)
	f.close()
	
def getTexTabLine(algorithm, ARI, homogeneity, completeness, vmeasure):
	return '{0} & {1:.3f} & {2:.3f} & {3:.3f} & {4:.3f} \\\\ \\hline\n'.format(algorithm, ARI, homogeneity, completeness, vmeasure)
	
def addToResult(algorithm, ARI, homogeneity, completeness, vmeasure):
	addLineToFile('result', getTexTabLine(algorithm, ARI, homogeneity, completeness, vmeasure))
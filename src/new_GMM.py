import drawing as draw
draw.savedImages = {}

import sys
import numpy as np
import pylab
import os
from sklearn import mixture
from sklearn.metrics import adjusted_rand_score, homogeneity_completeness_v_measure
from utils import data_to_na, parse_tab, addToResult


if len(sys.argv) < 3:
    sys.exit('Usage: python kmeans.py dataset k')
	
## Data preprocessing
data = parse_tab(sys.argv[1])
clusters = int(sys.argv[2])
classes = [example[-1] for example in data]
examples = data_to_na(data)

## Clustering
clf = mixture.GMM(n_components=clusters)
clf.fit(examples)
labels = clf.predict(examples)

## Performance evaluation
ari = adjusted_rand_score(labels, classes)
homogeneity, completeness, v_measure = homogeneity_completeness_v_measure(labels, classes)
print('ARI: {0}'.format(ari))
print('Homogeneity: {0}'.format(homogeneity))
print('Completeness: {0}'.format(completeness))
print('V-measure: {0}'.format(v_measure))
addToResult('GMM', ari, homogeneity, completeness, v_measure)


#x = np.linspace(min([x[0] for x in examples]), max([x[0] for x in examples]))
#y = np.linspace(min([y[1] for y in examples]), max([y[1] for y in examples]))
#X, Y = np.meshgrid(x, y)
#XX = np.c_[X.ravel(), Y.ravel()]
#Z = np.log(-clf.eval(XX)[0])
#Z = Z.reshape(X.shape)
#pylab.contour(Y, X, Z)

draw.scatter(examples, labels)
print(os.path.splitext(os.path.basename(sys.argv[1]))[0])
draw.setImgTitle('GMM_' + os.path.splitext(os.path.basename(sys.argv[1]))[0])
draw.showImage()
DiffNet
==============================
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.org/REPLACE_WITH_OWNER_ACCOUNT/DiffNet.png)](https://travis-ci.org/REPLACE_WITH_OWNER_ACCOUNT/DiffNet)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/DiffNet/branch/master/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/DiffNet/branch/master)

### Copyright

DiffNet is a Python tool for finding optimal allocations of sampling
in computational or experimental measurements of the individual
quantities and their pairwise differences, so as to minimize the covariance
in the estimated quantities.

DiffNet depends on CVXOPT (http://cvxopt.org) and networkx
(https://networkx.github.io/).  You can install these two libraries using
anaconda:

conda install -c conda-forge cvxopt
conda install -c anaconda networkx

DiffNet is free open source software.  NO WARRANTY, Use AS IS.


Some examples are provided in examples.py.

If you use DiffNet in a published work, please cite 

Huafeng Xu, Optimal measurement network of pairwise differences, 2019, https://arxiv.org/abs/1906.08599.

Copyright (C) 2018-2019 Huafeng Xu


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.0.

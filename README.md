# Anomalies
Implement the anomaly free solution of  [arXiv:1905.13729](https://arxiv.org/abs/1905.13729) [PRL]:

A set of integers $n_i$ ($i=1,2,\ldots,N$) satisfying the Diophantine equations
$$
 \sum_{i=1}^{N}n_i&=0\,,\qquad  \sum_{i=1}^{N}n_{i}^3&=0\,,
$$
can be parametrized as a function of two sets of integers $l$ and $k$, with dimensions $(N-3)/2$ and $(N-1)/2$ for $N$ odd, or $N/2-1$ and $N/2-1$ for $N$ even. 
The function is implemented below under the name: `free(l,k)`

## Install
```bash
$ pip install anomalies
```
## USAGE
```python
>>> from anomalies import anomaly
>>> anomaly.free([-1,1],[4,-2])
array([  3,   3,   3, -12, -12,  15])
>>> anomaly.free.gcd
3
>>> anomaly.free.simplified
array([ 1,  1,  1, -4, -4,  5])
```

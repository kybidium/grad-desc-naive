# grad-desc-naive

GRADDESC:
A very naive implementation of gradient descent for function approximation of sine based on a Khan Academy article. Aims to replicate the described process without prior knowledge of how these implementations are commonly done. Example of functional programming work. 

Visualizes difference between original function and approximatoin using matplotlib and numpy.

Inspired by a project in my Calculus III class, and thus transferred here from my college account (@luisojedacs). Choice of constants is arbitrary right now and implementation is not generalized to other functions.

Not fully optimized--arrives at an approximation after about 30 seconds with the current hard-coded final increment value; this happens far faster with a higher final increment value, but is less accurate. Current goals include generalizing the code for polynomials of random coefficients and allowing for optional command-line arguments for the final increment value, function interval, and polynomial coefficients or common function names (sin, cos, tan, etc.).

**To run**:
```
python3 graddesc.py
```
Then, the file 'plot.png' will be in the same directory and will depict the approximation as a red dotted line, with the actual sine function as a blue line.

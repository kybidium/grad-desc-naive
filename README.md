# grad-desc-naive

GRADDESC:
A naive, very inefficient implementation of gradient descent for polynomial approximation of sine. Aims to replicate the described process without prior knowledge of how gradient descent is normally implemented. Example of functional programming with Python, as well as use of numpy and matplotlib. 

Visualizes constrast between original function and approximation using matplotlib and numpy.

Not fully optimized--arrives at a visually-identical approximation after about 30 seconds with the current hard-coded final increment value; this happens far faster with a higher final increment value, but is less accurate. Current goals include generalizing the code for polynomials of random coefficients and allowing for optional command-line arguments for the final increment value, function interval, and polynomial coefficients or common function names (sin, cos, tan, etc.).

**To run**:
```
python3 graddesc.py
```
After the code is run, the file 'plot.png' will be saved to the same directory, depicting the approximation as a red dotted line, with the actual sine function as a blue line.

Inspired by a project in my Calculus III class, and thus initially transferred here from my college account (@luisojedacs).

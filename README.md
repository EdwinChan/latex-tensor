This LaTeX package typesets tensor indices and aligns them nicely. An example
is the geodesic equation:

```tex
\documentclass{article}
\usepackage{tensor}
\begin{document}
\[\frac{d\tensor u{^\mu}}{d\tau}
   +\tensor\Gamma{^\mu_\nu\rho}\tensor u{^\nu}\tensor u{^\rho}=0\]
\end{document}
```

The Python script `test-tensor.py` generates several PDFs which show the kinds
of tensors this package is capable of handling.

For everyday usage, we can declare a two-component tensor with
`\DeclareSimpleTensor\metric g2`, so `\metric\mu\nu` yields a tensor with two
covariant indices and `\metric*\mu\nu` yields a tensor with two contravariant
indices. We can also declare a two-component mixed tensor with
`\DeclareMixedTensor\kronm\delta`, so `\kronm\mu\nu` yields a tensor with the
first index contravariant and the second index covariant. Other minor options
can be discovered from the commented source.

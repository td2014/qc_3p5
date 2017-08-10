Quantum Mechanics
=================

To begin with, we will avoid philosophical debates about "quantum weirdness" in the document.  Whether or not the observations make sense based on our common-sense intuition is a separate topic.  The starting point for the approach in this work is to take the theory and resulting predictions, and compare them to experimental results to determine validity.

The other aspect will be to delve into various topics as deeply as necessary to extract the crucial elements.  This exploration may not be uniform in all cases.  In some aspects, deep-dives may be required or desired, and in others basic results or perhaps intermediate level results will be explored to assure reasonable understanding.

Quick Start
-----------

To jump into the basic ideas of Quantum Computation, it is worthwhile to introduce some basic notation, concepts, and an example calculation (inspired by Patrick Hayden video lecture I: https://sitp.stanford.edu/video/quantum-computational-universe-1-2).  In particular, let us focus the dicussion on a single "qubit" which is the fundamental element of a quantum mechanical computer.  We will discuss how computations can be done with a qubit later, but for now just assume that it is possible to extract a computational result using the qubit as a part of this operation.

We will consider that the qubit has basis states which form a linear vector space.  We are interested for now in qubits that have two possible basis states which are orthogonal (with the meaning exactly equivalent to the linear algebra terminology and concept).  We can represent these two states as 
:math:`\lvert0\rangle` and :math:`\lvert1\rangle`.  We can continue on to define :math:`\lvert+\rangle=\frac{1}{\sqrt{2}}(\lvert0\rangle+\lvert1\rangle)` and :math:`\lvert-\rangle=\frac{1}{\sqrt{2}}(\lvert0\rangle-\lvert1\rangle)`.

One immediate question is, can you construct and operator that can take a qubit in a given state and convert it to another?  This is an exercise.  

To be concrete, start with :math:`\lvert0\rangle` and place it into state :math:`\lvert+\rangle` by means of an operator.  To start simply, let us consider the following:

.. math::

   \begin{bmatrix}
      1 \\
      1 \\
   \end{bmatrix}
   =
   \begin{bmatrix}
      a && b \\
      c && d \\
   \end{bmatrix}
   \begin{bmatrix}
      1 \\
      0 \\
   \end{bmatrix}



A first quantum program.
------------------------

If we wish to use a quantum qubit to generate a random integer (0,1), we first will apply an operator to put it into a superposition state, and then we will make a measurement which will yield a 0 or 1.  Note that there is no way to predict ahead of time what this value will be.  Contrast this will the analogous operation on a classical computer.  Every random number will be a predictable result of a given input (through some sort of mapping function), which yields the idea of the pseudo-random sequence.  This is a key point, and is worth spending some time considering this aspect of quantum computation.


A quantum algorithm.
--------------------

Grover's algorithm is one of the basic building blocks that illustrate a quantum algorithm.  Basically, the algorithm allows for searching for a value in time :math:`O(\sqrt(n))` as opposed to a regular linear search :math:`O(n)`, in some array.  We'll go into the basic idea of the algorithm and then show an implementation using the ideas of the quantum gate operators.  The operators themselves will naturally follow from the earlier discussions about the quantum matrices as well will see.

However, we first present the Quantum Fourier Transform and then revisit Grover's algorithm.  The Fourier Transform is well-known in applications of signal processing as it provides for methods for analyzing signal content based on a transformation from time domain to frequency domain.  This had many uses such as a building block for speech recognition as an example.  Interestingly enough, the Fourier Transform also has applications in number theory, particularly in the realm of multiplication of large numbers.  The basic reason is that a product of two large numbers can be effectively carried out by a method called the Schömhage-Strassen algorithm (https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm) which relies on the fact that a convolution (which is effectively how a regular multiplication is done) can be efficiently computed using the product of two Fourier Transforms.

The basic formulation of the discrete Fourier transform, upon which the Quantum Fourier Transform is based is the following, where our notation and approach is after Coppersmiths work [Coppersmith1994].:

.. [Coppersmith1994] D. Coppersmith, An Approximate Fourier Transform Useful in Quantum Factoring. IBM Research Report.  July 1994.  Retrieved from https://arxiv.org/pdf/quant-ph/0201067.pdf

.. math::

  Y_{c} = \frac{1}{\sqrt{2^{L}}} \sum{a} X_{a} \exp(\frac{2 \pi i}{2^{L}} a c)

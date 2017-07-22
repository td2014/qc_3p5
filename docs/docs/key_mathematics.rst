Key Mathematics
===============

Linear Algebra
--------------


Tensor Networks
---------------

Some useful descriptions in what are termed "Tensor Networks" has been published recently (ref:  Orus, R. A Practical Introduction to Tensor Networks: Matrix Product States and Projected Entangled Pair States:  https://arxiv.org/abs/1306.2164 ).

To summarize, these tensor networks are a mathematical building block for describing quantum systems in a natural fashion, with network connections representing the couplings and entanglements of quantum systems.  One of the key aspects that is brought up in the above paper, and has an interesting analog in classical computation is the following.  Hilbert space, which represents the vector space of quantum states is exponential in complexity.  That is to say that for a practical sized system, say spin-:math:`1/2`, you will have :math:`2^{N}` states, with :math:`N` on the order of :math:`10^{23}`, since each quantum state can be in one of two values.  

This can be immediately considered an analogy to memory storage in a digital computer.  For example, consider a binary image that is 16x16 in size.  How many states can this represent?  The answer is :math:`2^{16\times16}` approximately the number of estimated particles in the known universe - :math:`10^{81}`.  If this is staggering enough, consider how long it would take to generate all possible states (1 or 0 at each pixel location) in such a 16x16 image.  Assume that we have a very fast computer which can update itself in a nano-second :math:`\approx 2^{-30}` seconds.  Therefore it would take approximately, :math:`2^{16\times16-30}` seconds which is about :math:`10^{68}` seconds.  This discussion parallels the comments made by Orus in regards to the Hilbert space in the above paper. 

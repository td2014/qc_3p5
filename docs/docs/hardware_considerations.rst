Hardware Considerations
=======================

We should delve more deeply into the hardware aspects of quantum computers and qubits.  The key element that needs to be implemented is one or more qubits along with appropriate circuitry or instrumentation to manipulate the qubits to perform computation.  Some of the challenges include being able to create a qubit which is stable for relatively long periods of time (ideally infinite) yet at the same time can instantly respong to a state change input or measurement input.

Josephson Junctions
-------------------

Before getting into the details of a fully built up quantum computer, it is useful to consider at some length the Josephson Junction.  Why?  Because, many practical qubits are constructed with Josephson Junctions as a key building block.  The Josephsen Junction, in the most simple terms, produces some sort of response (voltage or current) which is linearly proportional to the phase difference of the wave functions of two superconductors on either side of a barrier.  Thus, it is a linear frequency-to-voltage converter.  Also, it has the inverse capability by which it can be a voltage-to-frequency converter.  (ref: https://en.wikipedia.org/wiki/Josephson_effect).

How do we make a qubit using this device?  One approach is to construct a circuit which includes two Josephson Junctions which is coupled to magnetic flux which transits the loop area.  We'll explore this basic design.

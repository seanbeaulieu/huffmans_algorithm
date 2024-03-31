# Huffman's Compression Algorithm
 
One of the first times I really got to see the applications of math in regards to CS during my undergraduate was when Huffman's algorithm was taught. Of course, I understood the necessity of concepts like the hashtable, binary tree, sorting algorithms. However, expo marker math was never really that interesting to me until this algorithm. I thought it was so neat that you could encode data *using* the data structures we've spent so much time learning about.

With that being said, here's my writeup and implementation of the Huffman encoder, decoder, and file writer, written in Python. This will let you see how many bits get compressed using this algorithm. It also provides functions for writing out to a file and seeing the encoded text as well as the Huffman Code.

```
Enter text: Example text to use on my blog, one sentence only.
Encoded Text: 1101000001110101101100100010101001111100100000111001111100011111010010000100111011001111101100101111110111010100111101100101011101100110011100001000011100100001110111100111011001101001011101111
Huffman Codes: {'s': '0000', 'x': '0001', 'n': '001', 'p': '01000', 'u': '01001', ',': '01010', 'y': '01011', 'o': '011', 'e': '100', 'l': '1010', 'm': '10110', 'b': '101110', '.': '101111', 't': '1100', 'E': '110100', 'a': '110101', 'g': '110110', 'c': '110111', ' ': '111'}
Bits before compression (ASCII): 400
Bits after compression: 193
Bits saved: 207
Compression efficiency: 51.75%
```

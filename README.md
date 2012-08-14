elementdecoder
==============

Encodes and decodes strings with elements, to strings, using the element-number as a look up into the alphabet. 

Made this for a friend who needed it for the game 'The Secret World', where you must decode a page from a diary, written using this "encryption"

Example
=======
> % ./encoder.py this is a test 
>
> CaOFK FK H CaBKCa
>
> % ./decode.py CaOFK FK H CaBKCa
>
> THIS IS A TEST

What i basically did is in the c.py file i replaced y by b and in the b.py file i made sure when calling the function it was random_noise() and not random_noise.
To make sure the statement wasnt printed without deleting the print statement i simply placed the statement in the random_noise function.
since the function is ending with return something, the function will end when returning and therefore the print statement written after it will never be called. We can also import only the random_noise function from c and not anything else like the print statement however i found my method simpler

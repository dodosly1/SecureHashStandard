# SecureHashStandard
Code written in python for secure hash standard. It succesfully finds the message digest of SHA-256 and SHA-1. 
## Description
The Secure Hash Algorithms are a family of cryptographic hash functions published by the National Institute of Standards and Technology (NIST) as a U.S. Federal Information Processing Standard (FIPS), including:

SHA-0: A retronym applied to the original version of the 160-bit hash function published in 1993 under the name "SHA". It was withdrawn shortly after publication due to an undisclosed "significant flaw" and replaced by the slightly revised version SHA-1.

SHA-1: A 160-bit hash function which resembles the earlier MD5 algorithm. This was designed by the National Security Agency (NSA) to be part of the Digital Signature Algorithm. Cryptographic weaknesses were discovered in SHA-1, and the standard was no longer approved for most cryptographic uses after 2010.

SHA-2: A family of two similar hash functions, with different block sizes, known as SHA-256 and SHA-512. They differ in the word size; SHA-256 uses 32-bit words where 

SHA-512 uses 64-bit words. There are also truncated versions of each standard, known as SHA-224, SHA-384, SHA-512/224 and SHA-512/256. These were also designed by the NSA.

SHA-3: A hash function formerly called Keccak, chosen in 2012 after a public competition among non-NSA designers. It supports the same hash lengths as SHA-2, and its internal structure differs significantly from the rest of the SHA family.

The corresponding standards are FIPS PUB 180 (original SHA), FIPS PUB 180-1 (SHA-1), FIPS PUB 180-2 (SHA-1, SHA-256, SHA-384, and SHA-512). NIST has updated Draft FIPS Publication 202, SHA-3 Standard separate from the Secure Hash Standard (SHS).
## Impementation
This repository consists of three different files. 
1) The first file implements the functions that Sucure Hash Algorithms use. The functions of SHA algorithms operate on 32-bit words. Their existance is crucial because they will be used in the hashing procedure
2) There second file is essential for this project because it converts an ascii text to it's binary equivalent. Then it is followed by a procedure which turns this l bit message into chunck's of 512bit messages on which 512-bit the hashing function operate.
3) The third file implements the hashing function for Secure Hash algorithms. It uses takes an Array of 512-bit messages as an input an it produces an message digest which length depends on the secure hash algorithm that we are using. 
## How to use it
In order to use it you have to import the all repository files into your repository.
1) Use the preprocessing function to convert string to it's binary ascii equivalent.
2) Use SHA-256 or SHA-1 in order to calculate the message digest. 

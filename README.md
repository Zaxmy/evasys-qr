# Introduction
A quick hack to generate QR-codes with embedded links for in my use 
case evasys, but can be used for anything that expects a URL with an 
encoded argument.

## Inputs 
   * A CSV-file with PSWD values from example evasys 
   * URL that takes the value as an argument
## Outputs 
   * QR codes encoded as png pictures, one for each PSWD in input file.
   * A csv list with the header "pswd;@pswd_path". Where pswd is the 
    PSWD from the input file and @pswd_path is the full path to the 
    generated QR-code picture. The csv file can be used as mail merge 
    input in for example Adobe InDesign.

Implemented using Python 3.10.7 

Copyright Johan Zaxmy (2022)
Licensed under GPLv3

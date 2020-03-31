grid:


    ___|___|___
    ___|___|___
       |   |   


checking algo
    
      _00_|_01_|_02_
      _10_|_11_|_12_
       20 | 21 | 22 

    
    
    rows
        00 == 01 01 == 02 
        10 == 11 11 == 12
        20 == 21 21 == 22

    columns
        00 == 10 10 == 20
        01 == 11 11 == 21
        02 == 12 12 == 22

    diagonals
        00 == 11 11 == 22
        02 == 11 11 == 20

library
    numpy for arrays

functions
    wincheck
        passing for both p1,p2 with symbols


turns = 9
The purpose of this coding exercise is to utilize how a pattern for an object is created based on caluclation within a logic. In the past, a zip() funciton was applied to a for loop to get a pattern output. For this program, a nested for loop was applied to ensure  that the pattern output would be applied appropriately. 

The way the pattern output developed was from a nested for loop. The first loop is the top loop. This is the starting loop that applies the number of rows by the use of the range() function. Since the number of iteration is 5, the range(5+1 or 6) would be applied. 

The second inner loop is the first nested loop. So this is designated for the number of spaces. So in order to get the spaces, the number of iterations would be subtracted by last number of row, which would be 5-1, which would give you 4 spaces.

The third inner loop parallels the first nested loop, but is not the nested for loop for the second inner loop but, the first loop. This is where the pattern designation, "*", would be applied to the output design. This is where after the number of spaces, the pattern designation is applied. 

Here is a breakdown of the code via a conceptual design:

        iteration   |  i=(range(1,6))  |  j=(5-i)  | k=("*" * i)
            1               1             4= 5-1     k= "*" * 1
            2               2             3= 5-2     k= "*" * 2    
            3               3             2= 5-3     k= "*" * 3
            4               4             1= 5-2     k= "*" * 4
            5               5             0= 5-5     k= "*" * 5

The output then displays as such:

                                  *  
                                *  *  
                              *  *  *  
                             *  *  *  *  
                            *  *  *  *  *  

The best way to analyze the output is to take j and k, since i is implied. 

                            4= 5-1     k= "*" * 1
                            3= 5-2     k= "*" * 2
                            2= 5-3     k= "*" * 3
                            1= 5-2     k= "*" * 4
                            0= 5-5     k= "*" * 5

                           j=4      *     k=1 (see below for k)
                            j=3    *  *   k=2
                            j=2  *  *  *  k=3
                          j=1   *  *  *  *  k=4
                         j=0   *  *  *  *  *  k=5   


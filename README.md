# Problem
You are given a circular doubly linked list that contains integers as the data in each node. These data on each node is distinct. You have developed a special algorithm that prints the three continuous elements of the list, starting from the first element or head of the list and runs for infinite time.</br>
For example, if the list is `{1,9,12,7}`, then the output of the algorithm will be `{1,9,12,9,12,7,12,7,1,...}`. The output contains the infinite number of elements because it is a circular list.</br>

You are given only a part of the output that has been returned by the algorithm. Your task is to determine the number of elements available in the original list and print the respective elements.</br>

**Note**
> It is guaranteed that the provided part of the output of the algorithm is sufficient enough to calculate the size of the original list. 

## Input format

First line: Integer N that denotes the length of the list which is returned as the output of the algorithm
Next line: N space-separated integers that denote the elements of the list which is returned as the output of the algorithm
Output format

## Your task is to print the output in the following format:

First line: Length of the original list
Second line: Space-separated integers that denote the elements of the original list

## Constraints

1 <= N <= 10<sup>5</sup></br>
1<=A[i] <= 10<sup>9</sup>

## Sample Input
10</br>
7 12 8 12 8 13 8 13 7 13</br>

## Sample Output
4</br>
7 12 8 13</br>

## Explanation
The hidden list is actually [7,12,8,13] with 4 elements.</br>


**Note**
> You can see that the above list actually matches the output of the program.

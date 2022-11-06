# Longest-Bitonic-Subsequences
COSC 3320 HW3 Programming Challenge, Professor Wu

Call a sequence X[1..n] of numbers bitonic if there is an index i with 1 < i < n, such that the prefix X[1..i] is increasing and the suffix X [i .. n] is decreasing. Describe an efficient algorithm to compute the length of the longest bitonic subsequence of an arbitrary array X of integers.

Input format: first line is a single number n, the following line consists of n numbers that is the array A[1..n]

## Solution Explanation
The Longest Bitonic Sequence of a given array is the longest subsequence in which the subsequence’s elements are first in increasing order then in decreasing order.

To find it you'll need two subsequences
* Longest Increasing Subsequence
* Longest Decreasing Subsequence

We will find the LIS of the first half of our input of numbers so from [0...i]. And then we will find the LDS of our last half of our input of numbers, from [i...n].

The length of the Longest Bitonic Sequence is then the max of LIS[i] + LDS[i]-1.
Hence in our code we have:
	
	`LBS = max(LBS, LIS[i] + LDS[i]-1)`

We iterate through nums setting LBS to the max between itself and the value from the formula above. 

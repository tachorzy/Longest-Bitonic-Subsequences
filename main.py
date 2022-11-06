#!/usr/bin/env python

def longestIncreasingSubsequence(n, nums):
  LIS = [0 for elem in range(n)]
  LIS[0] = 1
  for i in range(1, n):
    for j in range(i):
      if nums[j] < nums[i] and LIS[j] > LIS[i]:
        LIS[i] = LIS[j]
    LIS[i] += 1
  return LIS

def longestDecreasingSubsequence(n, nums):
  LDS = [0 for elem in range(n)]
  LDS[n - 1] = 1
  for i in reversed(range(n - 1)):
    for j in reversed(range(i + 1, n)):
      if nums[j] < nums[i] and LDS[j] > LDS[i]:
        LDS[i] = LDS[j]
    LDS[i] += 1
  return LDS

def longestBitonicSequence(n, nums):
  if n == 0:
    return 0

  LIS = longestIncreasingSubsequence(n, nums)
  LDS = longestDecreasingSubsequence(n, nums)

  LBS = 1
  for i in range(n):
    LBS = max(LBS, LIS[i] + LDS[i] - 1)

  return LBS
  
def main():
  n = int(input())
  nums = [int(x) for x in input().split()]
  print(longestBitonicSequence(n, nums))

if __name__ == "__main__":
  main()

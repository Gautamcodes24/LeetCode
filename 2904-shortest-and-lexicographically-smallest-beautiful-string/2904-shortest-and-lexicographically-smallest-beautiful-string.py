class Solution:

  def shortestBeautifulSubstring(self, s: str, k: int) -> str:
    n = len(s)
    min_len = float("inf")
    ans = ""
    ones_count = 0
    l = 0

    for r in range(n):
      if s[r] == "1":
        ones_count += 1

      # Shrink window when we reach exactly k ones
      while ones_count == k:
        # Remove leading zeros to ensure the shortest valid window
        while s[l] == "0":
          l += 1

        sub = s[l : r + 1]
        curr_len = len(sub)

        # Update if we found a shorter substring, or an equal length one that is lexicographically smaller
        if curr_len < min_len or (curr_len == min_len and sub < ans):
          min_len = curr_len
          ans = sub

        # Move left pointer forward to check other candidates
        if s[l] == "1":
          ones_count -= 1
        l += 1

    return ans
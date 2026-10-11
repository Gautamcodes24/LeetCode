class Solution:

  def climbStairs(self, n: int) -> int:
    memo = {}

    def solve(steps):
      if steps == 1:
        return 1
      if steps == 2:
        return 2

      # Agar result pehle se calculate ho chuka hai, wahi se return karo
      if steps in memo:
        return memo[steps]

      # Result calculate karo aur memo me save karlo
      memo[steps] = solve(steps - 1) + solve(steps - 2)
      return memo[steps]

    return solve(n)
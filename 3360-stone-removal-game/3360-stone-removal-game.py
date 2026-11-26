class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        stones_to_remove = 10
        while n >= stones_to_remove:
            n = n - stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn
        return not alice_turn

        
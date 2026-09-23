class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unq = set()
        for e in emails:
            local , domain = e.split("@")
            local = local.split("+")[0].replace(".","")
            unq.add((local,domain))
        return len(unq)
        
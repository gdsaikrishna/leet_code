class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local,domain = email.split('@')
            local = local.replace('.',"")
            pos = local.find('+')
            if pos != -1:
                local = local[:pos]
            res.add(local+"@"+domain)
        return len(res)
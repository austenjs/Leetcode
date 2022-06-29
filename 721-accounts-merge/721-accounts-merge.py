class UnionFind:
    def __init__(self, N):
        self.parents = list(range(N))
    
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    
    def find(self, child):
        if child != self.parents[child]:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        union_find = UnionFind(N)
        
        email_to_id = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_id:
                    union_find.union(i, email_to_id[email])
                email_to_id[email] = i
    
        ans = collections.defaultdict(list)
        for email, id in email_to_id.items():
            ans[union_find.find(id)].append(email)
        
        return [[accounts[i][0], *sorted(emails)] for i, emails in ans.items()]
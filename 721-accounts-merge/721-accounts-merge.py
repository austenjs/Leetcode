from collections import defaultdict, deque

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create adj list
        adj_list = defaultdict(set)
        for name, *emails in accounts:
            for email1 in emails:
                for email2 in emails:
                    if email1 == email2:
                        continue
                    adj_list[email1].add(email2)
                    adj_list[email2].add(email1)
        
        ans = []
        added = set()
        for acc in accounts:
            name, email = acc[:2]
            if email in added:
                continue
            new_emails = []
            queue = deque([email])
            while queue:
                cur = queue.popleft()
                if cur in added:
                    continue
                new_emails.append(cur)
                added.add(cur)
                for neighbor in adj_list[cur]:
                    queue.append(neighbor)
            ans.append([name, *sorted(new_emails)])
        return ans 
"""
721. Accounts Merge

Given a list of accounts where each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some common email to both accounts.
Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts,
return the accounts in the following format:
the first element of each account is the name,
and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.
"""

"""
P - 1) create a adjacency list, which will list each email to emails
    2) create a primary email to name dictionary
    3) run DFS call to join associated emails in adjacency list under a single name
        a - create result to store results and visited to prevent email cycles
        b - define DFS call to join all related emails under allRelatedEmails
        c - make DFS call on every primary email and collect all related emails
        d - if primary email has not been seen then we should get all related emails under one name for storage
    4) return results
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create adjacency list of email to emails
        emailToEmails = defaultdict(set)

        # create email to name dictionary
        primaryEmailToName = dict()

        for account in accounts:
            # fill in primary email dict
            name = account[0]
            primaryEmail = account[1]
            primaryEmailToName[primaryEmail] = name

            # fill in the emailToEmails adjacency list
            for email in account[1:]:
                emailToEmails[primaryEmail].add(email)
                emailToEmails[email].add(primaryEmail)

        # run DFS call to join associated emails in adjacency list under a single name

        result = []
        visited = set()

        def dfs(email, allRelatedEmails):
            if email in visited:
                return
            visited.add(email)
            allRelatedEmails.add(email)
            relatedEmails = emailToEmails[email]
            for relatedEmail in relatedEmails:
                dfs(relatedEmail, allRelatedEmails)

        # make DFS call on every primary email and collect all related emails
        for primaryEmail, name in primaryEmailToName.items():
            allRelatedEmails = set()
            dfs(primaryEmail, allRelatedEmails)

            # if primary email has not been seen, then we should get all related emails under one name for storage
            if allRelatedEmails:
                result.append([name] + sorted(allRelatedEmails))

        return result
    # O(NK log NK) Time if all emails belong to one person, DFS will take N*K
    # O(N * K) space because building the adjacency list, the hash set, and the recursive call stacks each take O(N * K) space

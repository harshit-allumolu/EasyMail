"""

Author : Harshit Allumolu <allumoluharshit@gmail.com>

Functionality : To correct might-be spelling mistakes in the domain names in email addresses.

Idea : 

Let's dive into the code for more details!

"""

# TODO 1 : Check and correct email domains (use gramformer)
# TODO 2 : Find a way to check domain name exists or not


# import required modules


def LCS(X : str, Y : str) -> int:
    m = len(X)
    n = len(Y)
    L = [[None]*(n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]


def findAlternative(domain : str, domains : list) -> str:
    """
        Function name : findAlternative

        Arguments :
            -- domain (str type) : A domain name with less frequency
            -- domains (list type) : A list of all domains

        Returns :
            -- An alternative domain possible (str type)
    """
    newDomain = ""
    score = 0
    for d in domains:
        if d != domains:
            # longest common subsequence(LCS)
            length = LCS(domain, d)
            if length > score:
                score = length
                newDomain = d
    return newDomain


def correctAddress(emails : list) -> list:
    """
        Function name : correctAddress

        Arguments :
            -- emails : A list of all email IDs in the excel sheet
        
        Return :
            -- A list of email IDs with corrected domain names
    """
    threshold = 0.05     # tunable
    domains = [email[email.index("@")+1:] for email in emails]
    frequency = dict()
    for domain in domains:
        frequency[domain] = frequency.get(domain,0) + 1
    alternatives = dict()
    length = len(domains)
    for i in range(length):
        if frequency[domains[i]]/length <= threshold:
            if domains[i] in alternatives.keys():
                domains[i] = alternatives[domains[i]]
            else:
                alternative = findAlternative(domains[i], frequency.keys())
                domains[i] = alternative
                alternatives[domains[i]] = alternative
    newEmails = [emails[i][:emails[i].index("@")+1]+domains[i] for i in range(length)]
    return newEmails
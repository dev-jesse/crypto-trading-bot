def solution(input):
    unique_emails = set()

    for email in input:
        tmp = email.split('@')
        # Remove the .
        tmp[0] = ''.join(tmp[0].split('.'))
        # Remove the things after the +
        tmp[0] = tmp[0].split('+')[0]
        new_email = '@'.join(tmp).lower().strip()
        
        if new_email not in unique_emails: unique_emails.add(new_email)
        
    print(unique_emails)

    return len(unique_emails)

print(solution(["\"alexleet@code.com\"", " \"alex@leetcode.com\"", " \"a.lex.leet@code.com\"", " \"alex+leet@leetcode.com\""]))
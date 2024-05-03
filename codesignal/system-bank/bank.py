from heapq import heappop, heappush
from collections import deque
def solution(queries):
    ans  = []
    accounts = {}
    trans = {}
    pq = []
    payments_dq = deque()
    payment_counter = 0
    payment_statuses = {}
    for q in queries:
        ts = int(q[1])
        while payments_dq and ts >= payments_dq[0][0]:
            aid, payment_id, cashback_amount = payments_dq[0][1:]
            payments_dq.popleft()
            payment_statuses[aid][payment_id] = "CASHBACK_RECEIVED"
            print(payments_dq)
            accounts[aid]+= cashback_amount
        if q[0] == 'CREATE_ACCOUNT':
            if q[2] in accounts:
                ans.append("false")
            else:
                accounts[q[2]] = 0
                trans[q[2]] = 0
                payment_statuses[q[2]] = {}
                heappush(pq, (-0, q[2]))
                ans.append("true")
        elif q[0] == 'DEPOSIT':
            aid, amt = q[2], q[3]
            if aid not in accounts:
                ans.append("")
            else:
                accounts[aid]+= int(amt)
                ans.append(str(accounts[aid]))
        elif q[0] == 'TRANSFER':
            
            # print(q[1], accounts)
            sid, tid, amt = q[2], q[3], int(q[4])
            if tid ==sid or sid not in accounts or tid not in accounts or accounts[sid] < amt:
                ans.append('')
            else:
                accounts[tid]+= amt
                accounts[sid]-= amt
                
                ans.append(str(accounts[sid]))
                trans[sid]+= amt
                heappush(pq, (-trans[sid], sid))
                
        elif q[0] == 'TOP_SPENDERS':
            res = []
            n = int(q[2])
            while n and pq:
                # print
                tmt, aid = -pq[0][0], pq[0][1]
                heappop(pq)
                if tmt !=  trans[aid]: continue
                res.append((aid, tmt))
                n-= 1
            for aid, tmt in res:
                heappush(pq, (-tmt, aid))

            ans.append(', '.join([ f'{aid}({tmt})' for aid, tmt in res]))
       
        elif q[0] == 'PAY':
            ts, aid, amt = int(q[1]), q[2], int(q[3])
            if aid not in accounts or accounts[aid] < amt:
                ans.append('')
            else:
                payment_counter += 1
                payment_id = f"payment{payment_counter}"
                accounts[aid] -= amt
                trans[aid]+= amt
                heappush(pq, (-trans[aid], aid))

                cashback_amount = amt // 50  # 2% cashback
                payments_dq.append([ts + 86400000, aid, payment_id, cashback_amount])
                payment_statuses[aid][payment_id] = "IN_PROGRESS"

                ans.append(payment_id)

        
        elif q[0] == 'GET_PAYMENT_STATUS':
            ts, aid, payment_id = int(q[1]), q[2], q[3]
            if aid not in accounts or payment_id not in payment_statuses[aid]:
                ans.append('')
            else: ans.append(payment_statuses[aid][payment_id])
    return ans
            
# [
#   "true",
#   "true",
#   "2000",
#   "1000",
#   "payment1",
#   "payment2",
#   "payment3",
#   "payment4",
#   "1600",
#   "600",
#   "1702",
#   "700"
# ]

# The banking system should support merging two accounts while retaining both accounts' balance and transaction histories.

# MERGE_ACCOUNTS <timestamp> <accountId1> <accountId2> — should merge accountId2 into the accountId1. Returns "true" if accounts were successfully merged, or "false" otherwise. Specifically:

# Returns "false" if accountId1 is equal to accountId2.
# Returns "false" if accountId1 or accountId2 doesn't exist.
# All pending cashback refunds for accountId2 should still be processed, but refunded to accountId1 instead.
# After the merge, it must be possible to check the status of payment transactions for accountId2 with payment identifiers by replacing accountId2 with accountId1.
# The balance of accountId2 should be added to the balance for accountId1.
# TOP_SPENDERS operations should recognize merged accounts - the total outgoing transactions for merged accounts should be the sum of all money transferred and/or withdrawn in both accounts.
# accountId2 should be removed from the system after the merge.
# GET_BALANCE <timestamp> <accountId> <timeAt> — should return a string representing the total amount of money in the account accountId at the given timestamp timeAt. If the specified account did not exist at a given time timeAt, returns an empty string.

# If queries have been processed at timestamp timeAt, GET_BALANCE must reflect the account balance after the query has been processed.
# If the account was merged into another account, the merged account should inherit its balance history.
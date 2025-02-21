from collections import *
class Invoicer:
    def __init__(self, schedule):
        self.schedule = schedule
    def send_emails1(self, invoices):
        ans = []
        for x in invoices:
            time, name, a = x['invoice_time'], x['name'], x['amount']
            for offset, tp in self.schedule.items():
                ans.append([time+offset, tp, name, a])
        ans.sort()
        ansstr = [ f"{time}: [{tp}] Invoice for {name} for {a} dollars" for time, tp, name, a in ans]
        return ansstr
    def send_emails(self, invoices, payments):
        ans = []
        m = {}
        for x in invoices:
            time, name, a = x['invoice_time'], x['name'], x['amount']
            m[name] = a
            for offset, tp in self.schedule.items():
                ans.append([time+offset, tp, name, a])
        for x in payments:
            time, name, a = x['payment_time'], x['name'], x['amount']
            ans.append([time, '', name, a])
        ans.sort()

        for i, (time, tp, name, a) in enumerate(ans):
            if len(tp) == 0:
                m[name]-= a
            else:
                ans[i][-1] = m[name]
        ansstr = [ f"{time}: [{tp}] Invoice for {name} for {a} dollars" for time, tp, name, a in ans if len(tp) and a]
        names = []
        for name, a in m.items():
            if a:
                names.append((name, a))
        names.sort()
        # "Delinquent customers:",
        # "Alice owes 50 dollars"
        if names:
            ansstr.append("Delinquent customers:")
            for name, a in names:
                ansstr.append(f"{name} owes {a} dollars")
        for l in ansstr:
            print(l)
        return ansstr


def test_send_emails():
    send_schedule = {
        -10: "Upcoming",
        0: "New",
        20: "Reminder",
        30: "Due"
    }
    invoicer = Invoicer(send_schedule)

    customer_invoices = [
        {"invoice_time": 0, "name": "Alice", "amount": 200},
        {"invoice_time": 1, "name": "Bob", "amount": 100},
    ]
    
    expected_output = [
        "-10: [Upcoming] Invoice for Alice for 200 dollars",
        "-9: [Upcoming] Invoice for Bob for 100 dollars",
        "0: [New] Invoice for Alice for 200 dollars",
        "1: [New] Invoice for Bob for 100 dollars",
        "20: [Reminder] Invoice for Alice for 200 dollars",
        "21: [Reminder] Invoice for Bob for 100 dollars",
        "30: [Due] Invoice for Alice for 200 dollars",
        "31: [Due] Invoice for Bob for 100 dollars",
    ]
    
    assert invoicer.send_emails1(customer_invoices) == expected_output, "Test Case 1 Failed"
    print("Test Case 1 Passed")
    
    # Additional test cases for Part 1
    customer_invoices_extra = [
        {"invoice_time": 2, "name": "Eve", "amount": 300},
    ]
    expected_output_extra = [
        "-8: [Upcoming] Invoice for Eve for 300 dollars",
        "2: [New] Invoice for Eve for 300 dollars",
        "22: [Reminder] Invoice for Eve for 300 dollars",
        "32: [Due] Invoice for Eve for 300 dollars",
    ]
    assert invoicer.send_emails1(customer_invoices_extra) == expected_output_extra, "Test Case 1.1 Failed"
    print("Test Case 1.1 Passed")
    
    # Another additional test case for Part 1
    customer_invoices_more = [
        {"invoice_time": 5, "name": "David", "amount": 400},
    ]
    expected_output_more = [
        "-5: [Upcoming] Invoice for David for 400 dollars",
        "5: [New] Invoice for David for 400 dollars",
        "25: [Reminder] Invoice for David for 400 dollars",
        "35: [Due] Invoice for David for 400 dollars",
    ]
    assert invoicer.send_emails1(customer_invoices_more) == expected_output_more, "Test Case 1.2 Failed"
    print("Test Case 1.2 Passed")

def test_send_emails_with_payments():
    send_schedule = {
        -10: "Upcoming",
        0: "New",
        20: "Reminder",
        30: "Due"
    }
    invoicer = Invoicer(send_schedule)

    customer_invoices = [
        {"invoice_time": 0, "name": "Alice", "amount": 200},
        {"invoice_time": 1, "name": "Bob", "amount": 100},
    ]
    
    customer_payments = [
        {"payment_time": -9, "name": "Alice", "amount": 100},
        {"payment_time": 1, "name": "Alice", "amount": 50},
        {"payment_time": 0, "name": "Bob", "amount": 100},
    ]
    

# 0: [New] Invoice for Alice for 100 dollars
# 1: [New] Invoice for Bob for 100 dollars
# 20: [Reminder] Invoice for Alice for 150 dollars
# 21: [Reminder] Invoice for Bob for 100 dollars
# 30: [Due] Invoice for Alice for 150 dollars
# 31: [Due] Invoice for Bob for 100 dollars
# 0: [New] Invoice for Alice for 100 dollars
# 1: [New] Invoice for Bob for 100 dollars
# 20: [Reminder] Invoice for Alice for 150 dollars
# 21: [Reminder] Invoice for Bob for 100 dollars
# 30: [Due] Invoice for Alice for 150 dollars
# 31: [Due] Invoice for Bob for 100 dollars
# Delinquent customers:
# Alice owes 150 dollars
# Bob owes 100 dollars
    expected_output = [
        "-10: [Upcoming] Invoice for Alice for 200 dollars",
        "-9: [Upcoming] Invoice for Bob for 100 dollars",
        "0: [New] Invoice for Alice for 100 dollars",
        "20: [Reminder] Invoice for Alice for 50 dollars",
        "30: [Due] Invoice for Alice for 50 dollars",
        "Delinquent customers:",
        "Alice owes 50 dollars"
    ]
    
    assert invoicer.send_emails(customer_invoices, customer_payments) == expected_output, "Test Case 2 Failed"
    print("Test Case 2 Passed")
    
    # Additional test cases for Part 2
    customer_payments_extra = [
        {"payment_time": -5, "name": "Eve", "amount": 150},
    ]
    expected_output_extra = [
        "-10: [Upcoming] Invoice for Alice for 200 dollars",
        "-9: [Upcoming] Invoice for Bob for 100 dollars",
        "-5: [Upcoming] Invoice for Eve for 300 dollars",
        "0: [New] Invoice for Alice for 100 dollars",
        "20: [Reminder] Invoice for Alice for 50 dollars",
        "30: [Due] Invoice for Alice for 50 dollars",
        "Delinquent customers:",
        "Alice owes 50 dollars",
        "Eve owes 150 dollars"
    ]
    
    assert invoicer.send_emails(customer_invoices, customer_payments_extra) == expected_output_extra, "Test Case 2.1 Failed"
    print("Test Case 2.1 Passed")
    
    # Another additional test case for Part 2
    customer_payments_more = [
        {"payment_time": 0, "name": "David", "amount": 400},
    ]
    expected_output_more = [
        "-10: [Upcoming] Invoice for Alice for 200 dollars",
        "-9: [Upcoming] Invoice for Bob for 100 dollars",
        "0: [New] Invoice for Alice for 100 dollars",
        "20: [Reminder] Invoice for Alice for 50 dollars",
        "30: [Due] Invoice for Alice for 50 dollars",
        "Delinquent customers:",
        "Alice owes 50 dollars"
    ]
    
    assert invoicer.send_emails(customer_invoices, customer_payments_more) == expected_output_more, "Test Case 2.2 Failed"
    print("Test Case 2.2 Passed")



test_send_emails()
test_send_emails_with_payments()

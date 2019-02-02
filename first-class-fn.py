def creator(msg):
    def borrower():
        print("I borrowed this from creator:", msg)
    return borrower
result = creator('lender')
result()
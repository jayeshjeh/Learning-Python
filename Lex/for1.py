
no_of_pass = 5
no_of_bagg = 2
security_check = True

for pass_count in range(1, no_of_pass+1):
    for bagg_count in range(1, no_of_bagg+1):
        if security_check:
            print("Security check of passenger: ", pass_count, "Bags cleared: ", bagg_count)
        else:
            print("Security check of passenger: ", pass_count, "Bags not cleared: ", bagg_count)


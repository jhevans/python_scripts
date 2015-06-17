# A demonstration of Python's differing behaviour when naming small and large ints

low_int_1 = 1
low_int_2 = 0 + 1
print("low int equals:")
print(low_int_1 == low_int_2)
print("low int is:")
print(low_int_1 is low_int_2)
print("\n")

high_int_1 = 12345
high_int_2 = 12344 + 1

print("high int equals:")
print(high_int_1 == high_int_2)
print("high int is:")
print(high_int_1 is high_int_2)

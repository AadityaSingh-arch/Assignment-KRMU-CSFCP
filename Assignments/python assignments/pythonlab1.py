# Program to generate specific outputs from the string 'Shenanigan'
s = 'Shenanigan'

# 1. Sh
print(s[:2])
# 2. an
print(s[2:4])
# 3. enanigan
print(s[2:])
# 4. Shenan
print(s[:6])
# 5-8. Shenan (printed 4 times)
for _ in range(4):
	print(s[:6])
# 9. Shenanigan
print(s)
# 10. Snin
print(s[0] + s[2] + s[4] + s[8])
# 11. Saa
print(s[0] + s[2] + s[2] + s[1])
# 12. Shenanigan Type
print(s + ' Type')
# 13. ShenanWabbite
print(s[:6] + 'Wabbite')

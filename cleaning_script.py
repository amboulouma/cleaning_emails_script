input_file = input("Enter name of input file: ")
output_file = input("Enter name of output file: ")
emails = set()
input_f = open(input_file, 'r')
output_f = open(output_file, 'w')
for line in input_f:
	for email in line.split(' '):
		if '@' in email:
			emails.add(email)
input_f.close()
for email in emails:
	if email.endswith('\n'):
		output_f.write(email)
		continue
	else:
		output_f.write(email+'\n')
output_f.close()

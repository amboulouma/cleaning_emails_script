input_file = input("Enter name of input file: ")
output_file = input("Enter name of output file: ")
emails = set()
input_f = open(input_file, 'r')
output_f = open(output_file, 'w')
for line in input_f:
	for email in line.split(' '):
		if '@' in email:
			emails.add(email)
for email in emails:
    output_f.write(email+'\n')
input_f.close()
output_f.close()

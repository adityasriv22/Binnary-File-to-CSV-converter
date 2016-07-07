from os.path import exists
print "Type the Filename: "
input_file = raw_input('::')
output_file = open("binascii_out.csv","wb")
if exists(input_file):
	in_file = open(input_file,"r")
	output_str = in_file.read()
else:
	print "No such file found"
i = 0
result_str =""
for i in range(0,len(output_str)):
	if i%8 == 0: #conversion only takes place at when i is a multiple of 8
		result_str = result_str +  chr(int(output_str[i:i+8],2))
output_file.write(result_str)
output_file.close()

"""
BSD 3-Clause License

Copyright (c) 2023, Özlem Salman
Copyright (c) 2023, Armağan Salman

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


#(
# Python system modules:
import itertools
#)

#(
# 3rd party modules:
import Bio
#)

#(
# Local modules:
import csv_file_io as Csvio
#)


def get_grouped_data(data_file_path, group_key_func = None):
#(
	if group_key_func == None:
	#(
		# By default, use activation class as group key
		group_key_func = lambda x: x[2]
	#)
	data_with_header = Csvio.read_data_from_csv(data_file_path)
	data = data_with_header[1:] # Skip data header
	
	# activation class string might have spaces. strip them:
	data_iter = map(lambda r: [r[0], r[1], r[2].strip()] , data)
	
	# Sorting is necessary for itertools.groupby
	sorted_data = sorted(data_iter, key = lambda x: x[2]) # x[2] = activation class
	
	return itertools.groupby(sorted_data, key = lambda x: x[2])
#)


def select_rows_by_min_seqlen(data_rows, desired_min_len, desired_max_len):
#(
    """ row = id, sequence, activation class string
    """
    
    selected_rows = []
    for rw in data_rows:
    #(
        seq = rw[1]
        if len(seq) >= desired_min_len and len(seq) <= desired_max_len:
            selected_rows.append(rw)
        
    #)      
    return selected_rows
#)


def main(args):
#(
    #mod. active ile inactive exp gruplarından 80'er tane row alınıp, her row karşısındaki row ile karşılaştırılacak
    
	first_file = args["first_sequence_file"]
	second_file = args["second_sequence_file"]
	
	get_class_value = lambda x: x[2]
	grouped_class = get_grouped_data(first_file, group_key_func = get_class_value)
	
	for key, group in grouped_class:
	#(
		print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
		print(key)
		for x in group:
		#(
			print(x)
		#)
		print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
	#)
	
	
	print("Executed main.")
#)


if __name__ == "__main__":
#(
	args = dict()
	
	f = "ACPs_Breast_cancer.csv"
	sf = "ACPs_Lung_cancer.csv"
	assert(f != sf)
	
	args["first_sequence_file"] = f
	args["second_sequence_file"] = sf
	
	main(args)
#)



"""
select_by_seqlen("data.csv", 12)
select_by_seqlen("data.csv", 15)
select_by_seqlen("data.csv", 20)
select_by_seqlen("data.csv", 3)
"""

"""
#peptitleri uzunluğuna göre alınacak, aşağıdaki de dosya okumak için
    data_with_header = Csvio.read_data_from_csv(csv_file_path)
	rows = data_with_header[1:]
"""
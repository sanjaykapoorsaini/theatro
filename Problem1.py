"""
Problem 1
---------

Alex and Bob are high-school friends, and are enthusiastic about secret messages.
They design their own algorithm for encrypting messages.
Suppose Alex wants to send Bob the message: "canyoudecryptthismessage?", he starts out
by deciding on a number, `X` [ 0 < X < the length of the message ], as the number of columns
and generates a matrix, by writing each character top-to-down in columns, starting
with the first cell, then the second column, and so on to form a matrix.
Then he writes the output string on a single line by copying characters from this matrix,
left-to-right and right-to-left, in odd and even rows.

         input:    "canyoudecryptthismessage?"

transformation:    c u y i s       // X = number_of_columns = 5
                   a d p s a
                   n e t m g
                   y c t e e
                   o r h s ?

        output:    "cuyisaspdanetmgeetcyorhs?"

Given the output, write a program that calculates the `X` (number_of_columns), and
also decrypts the message to obtain the original message.

OWNER - SANJAY

"""
    

def getAllPossibleSolutions(message):
    """Provides all possible combination of solutions messages """    
    
    for columns in xrange(2, len(message)):                                    #loop for column 1 to length of the string
        output = ""
        rows_length = int(round(len(message) / float(columns)))                #convert the column to float to get the round value e.g. for 2.6 we get 3 now
        for row_num in xrange(rows_length):                                                 
            row = message[row_num::rows_length]                                #get transformation row using slicing  
            if row_num % 2 == 0:  output += row                                #check for even rows               
            else: output += row[::-1]                                          #reverse the odd rows
            
        print  "X = " + str(columns) + "  Output is --> " + str(output)      



if __name__ == '__main__':
    message = str(raw_input('Please enter the encrypted message... '))
    print  "X = " + str(1) + "  Output is --> " + str(message)                 #output will be same for 1 column :)
    getAllPossibleSolutions(message)

#filename: Decipher.py
#author: Goh Jia ying

try:
    mystery_file = open('MYSTERY.IN', 'r')
    outfile = open('MYSTERY.TXT','r')
    line = mystery_file.readlines()
    
    #def fibonnaci function:
##    def fibonacci_generator():
##        num = 1
##        new_num =

    #def ascii shift function, shift by 5
    def ascii_shift(string):
        str_string = str(string)
        new_string = ""
        for i in str_string:
            new_chr_no = ord(i) -5
            new_chr = chr(new_chr_no)
            new_string = new_string + str(new_chr)
        print(new_string)
            
    #try decripting...
    text =  str(ascii_shift(line))
    word =  text.split(' ')
    print(word + "\n")

    #def a count word function
##    def count_word(text,word):
        
        
        
        
    outfile_.close()
    mystery_file.close()
    
except IOError:
    print("File MYSTERY.IN cannot be read or MYSTERY.TXT cannot be written")

#filename: Decipher.py
#author: Goh Jia ying
def ascii_shift(string):
        
    new_string = ""
    for i in string:
        new_chr_no = ord(i) - 5
        new_chr = chr(new_chr_no)
        new_string = new_string + new_chr
    return (new_string)
            
try:
    mystery_file = open('MYSTERY.IN', 'r')
    outfile = open('MYSTERY.TXT','w')
    line = mystery_file.readlines()
    
##    #def fibonnaci function:
##    def fibonacci_generator():
##        num = 1
##        new_num =



    #def ascii shift function, shift by 5
    
    #try decripting...
    for row in line: # important line cannot directlyjust print line as \n will be printed
        print(ascii_shift(row))
    word =  text.split(' ')
##    print(word + "\n")

    #def a count word function
##    def count_word(text,word):
        
        
        
        
    outfile_.close()
    mystery_file.close()
    
except IOError:
    print("File MYSTERY.IN cannot be read or MYSTERY.TXT cannot be written")


import pandas as pd
import re
 
 
digit_regex = re.compile(r"(\d{1})")

word_to_digit = {
    "one": "1",
    "two": "2", 
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}



silly_string = ""
for k,v in word_to_digit.items():
    silly_string = silly_string+ k+"|"

silly_string+="\d{1}"
silly_string = "("+silly_string+")"
full_regex = re.compile(silly_string)

#Regex to search string from reverse
word_to_word_reversed = {}
for k,v in word_to_digit.items():
    word_to_word_reversed[k[::-1]]=k

silly_string_reversed = ""
for k,v in word_to_word_reversed.items():
    silly_string_reversed = silly_string_reversed + k+"|"
    
silly_string_reversed+="\d{1}"
silly_string_reversed = "("+silly_string_reversed+")"
reverse_regex = re.compile(silly_string_reversed)
    
    
 
#part 1
def retrieve_calibration(input_text):
    df = input_text
    df2 = df.apply(get_2_digits, axis=1)
    return(df2["two_digits"].sum())


def get_2_digits(row):
    search = digit_regex.findall(row["line"])
    first_and_last_digits = search[0] + search[-1]
    row["two_digits"] = int(first_and_last_digits)
    return row

def get_2_digits_full_regex_lazy(row):
    search = full_regex.findall(row["line"])
    reverse_search = reverse_regex.findall(row["line"][::-1])
    first_digit = search[0]
    last_digit=reverse_search[0]
    for k,v in word_to_word_reversed.items():
        if k in last_digit:
            last_digit = last_digit.replace(k,v)
    
    first_and_last_digits=first_digit+last_digit
    
    for k,v in word_to_digit.items():
        if k in first_and_last_digits:
            first_and_last_digits=first_and_last_digits.replace(k,v)
    
    row["two_digits"] = int(first_and_last_digits)
    return row
    

#part 2

def retrieve_calibration_with_words(input_text):
    df = input_text
    df2 = df.apply(get_2_digits_full_regex_lazy, axis=1)
    return(df2["two_digits"].sum())
    


def sub_words_for_digits(row):
    for key, value in word_to_digit.items():
        if key in row["line"]:
            row["line"]=row["line"].replace(key,value)
    return row
    
with open("source\day_01\part_1_input.txt") as input_txt:
    df = pd.read_csv(input_txt, sep=" ", header=None, names=["line"])
    print(retrieve_calibration(df))
    print(retrieve_calibration_with_words(df))
    


import glob
import re


def usage():
    print("Usage: findarmstrongs –d directory [–[a|h|n|r|t|v]]"
          "The program searches for text files in the given directory and sub-directories and prints the following information based on the given flag parameters:"
          "\nWhere:"
          "\n\t–a: prints all armstrong numbers found in the text files"
          "\n\t–h: prints this usage message"
          "\n\t–n: prints the total number of armstrong numbers found. This is the default behavior when running the program with no flags"
          "\n\t–r: prints the number of files that contain armstrong numbers"
          "\n\t–t: prints the total number of text files found"
          "\n\t–v: is equivalent to running the program with –anrt")


def find_files(directory):
    return glob.glob(directory + "/**/*.txt", recursive=True)


def is_armstrong(number):
    temp = number
    length = len(str(number))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10

    return sum == number


def find_armstrong_in_file(text_file):
    armstrong_in_file = []
    with open(text_file, 'r') as file:
        for line in file:
            for word in re.split(',|_|-|!| |\.', line):
                cleaned_word = word.strip()
                if cleaned_word.isdigit() and is_armstrong(int(cleaned_word)):
                    armstrong_in_file.append(int(cleaned_word))
    return armstrong_in_file


def find_armstrong_in_path(directory):
    text_files = find_files(directory)
    armstrongs_numbers = []

    for text_file in text_files:
        armstrongs_numbers.append(find_armstrong_in_file(text_file))

    return armstrongs_numbers


def number_of_files_with_armstrong(directory):
    text_files = find_files(directory)
    files_counter = 0

    for text_file in text_files:
        if len(find_armstrong_in_file(text_file)) > 0:
            files_counter += 1

    return files_counter


def find_armstrong(params):
    directory = params['directory']
    answer = {}
    if 'h' in params:
        answer['usage'] = usage()
    if 'a' or 'v' in params:
        answer['armstrong_numbers'] = find_armstrong_in_path(directory)
    if 'n' or 'v' in params:
        answer['number_of_armstrong_numbers'] = len(find_armstrong_in_path(directory))
    if 'r' or 'v' in params:
        answer['number_of_files'] = number_of_files_with_armstrong(directory)
    if 't' or 'v' in params:
        answer['text_files'] = len(find_files(directory))

    return answer

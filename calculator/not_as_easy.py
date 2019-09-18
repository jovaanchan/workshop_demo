# function returns a reversed value of arg1's digits
def reverse_digits(arg1):
  #========================================#
  # input: integer arg1                    #
  # return: integer or string              #
  # eg. input: 632527 => return: 725236    #
  #========================================#
   return reverse(arg1)


# function returns a sorted value of arg1's digits
def sort_digits(arg1):
  #========================================#
  # input: integer arg1                    #
  # return: integer or string              #
  # eg. input: 632527 => return: 223567    #
  #========================================#
    numstr = str(arg1)
    return sorted(numstr)

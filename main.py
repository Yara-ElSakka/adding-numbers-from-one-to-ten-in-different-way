# this is a code question from the Math Olympiad
# this is another way.
# By : Yara Elsakka

start_num = int(input("please enter the start number: "))
end_num = int(input("please enter the end number: "))

if end_num % 2 == 0:  # end number is even. there is a middle number.
    couple_num = end_num / 2
    couple_value = end_num
    middle_num = end_num / 2
    total_final = (couple_num * couple_value) + middle_num
    print("(END NUM is EVEN) the sum of numbers between ", start_num, "and ", end_num, "is equal to ", total_final)
else:  # end number is odd. there is no middle number.
    couple_num = (end_num - 1) / 2
    couple_value = end_num
    middle_num = end_num / 2
    total_final = couple_num * couple_value
    print("(END NUM is ODD) the sum of numbers between ", start_num, "and ", end_num, "is equal to ", total_final)
# end of code

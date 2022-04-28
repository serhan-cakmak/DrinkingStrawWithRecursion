
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


#almost all functions do the same thing with same logic which is indicating another variable inside the func which enables us to iterate and return the necessary numbers to the other functions

##########actually this 1.1 func does the same thing with 2.1 but while I was writing the code I didn't want to change the already working func so I didn't delete this
def func1_1(a):
    if a==0:
        return
    print(" ", end="")
    func1_1(a-1)
#This func 1 just prints out the straw over the glass
def func1(straw_pos,a,last_oplace,x=0):
    if straw_pos==x:
        return last_oplace
    func1_1(a)
    print("o")
    return func1(straw_pos,a+1,last_oplace+1,x+1)

#this func just prints out the necessary space charecters
def func2_1(space_number,x=0):
    if space_number==x:
        return space_number
    print(" ", end="")
    return func2_1(space_number,x+1)
#this func prints out the empty side of glass
def func2(real,space_number,last_oplace,dont_brakeglass,total_line_length,x=0):
    if x==real:
        return space_number,last_oplace,dont_brakeglass   #if I don't return these values main func won't work well and will crack
    #if brakeglass ==False that means I have to stop all the code and return immediately
    if dont_brakeglass==False:
        return space_number,last_oplace,dont_brakeglass
    func2_1(space_number)
    print("\\", end="")
    spaces_before_o = last_oplace - 2 - space_number
    func2_1(spaces_before_o)
    print("o", end="")
    spaces_after_o = total_line_length - 2 * space_number - 1 - spaces_before_o - 1 - 1

    if spaces_after_o < 2:
        dont_brakeglass = False #if I would have returned the brakeglass value from this code, there will be an error


    func2_1(spaces_after_o)
    print("/")

    return func2(real,space_number+1,last_oplace+1,dont_brakeglass,total_line_length,x+1)  #If I wouldn't return this func I cannot obtain the values I will need




#star printer

def func3_2(star_wide,x=0):
    if star_wide==x:
        return
    print("*", end="")
    func3_2(star_wide,x+1)


def func3(filled_line_range,glass_size,space_number,x=0):
    if filled_line_range==x:
        return space_number


    func2_1(space_number)

    print("\\", end="")
    star_wide = 2 * glass_size - 2 * space_number
    func3_2(star_wide)

    print("/")


    return func3(filled_line_range,glass_size,space_number+1,x+1)

#just prints out the lower part of the glass
def func5(glass_size,x=0):
    if glass_size==x:
        return

    func2_1(glass_size)
    print("||")
    func5(glass_size,x+1)



#this is the main func which prints out the whole glass over and over again
def func6(real,glass_size,straw_pos,x=0):
    if real==x:
        return
    last_oplace = 1
    total_line_length = 2 * glass_size + 2
    space_number = 0
    a = 0
    dont_brakeglass = True

    #Both printing and returning a value
    last_oplace = func1(straw_pos, a, last_oplace)
    # Both printing and returning a value
    space_number, last_oplace, dont_brakeglass = func2(x, space_number, last_oplace, dont_brakeglass,total_line_length)

    filled_line_range = glass_size - x
    # Both printing and returning a value, however it seems like this value does nothing
    space_number = func3(filled_line_range, glass_size, space_number)

    func2_1(glass_size)
    print("--")

    func5(glass_size)
    # I am checking whether this should be the last printing before glass having broken or not
    if dont_brakeglass==False:
        return

    return func6(real,glass_size,straw_pos,x+1)

real=glass_size+1
#and here we recall just one main function
func6(real,glass_size,straw_pos)



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


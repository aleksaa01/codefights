def validTime(time):
    hours, minutes = time.split(':')

    return ('0' <= hours <= '23') and ('0' <= minutes <= '59')


"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

    For time = "13:58", the output should be
    validTime(time) = true;
    For time = "25:51", the output should be
    validTime(time) = false;
    For time = "02:76", the output should be
    validTime(time) = false.

"""
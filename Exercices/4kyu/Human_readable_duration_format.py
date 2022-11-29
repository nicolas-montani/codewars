'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''

def format_duration(seconds):
    #your code here
    if seconds == 0: 
        return "now"
    
    print(seconds)
    
    years = seconds//31_536_000
    days = seconds//86_400 - 365*years
    hours = (seconds - 31_536_000*years - 86_400*days)//3600
    minutes = (seconds - 31_536_000*years - 86_400*days - 3600*hours)//60
    second = seconds%60 
    
    
    print(years)
    print(days)
    print(hours)
    print(minutes)
    print(second)

    
    if second == 0 : 
        sec = ''
    elif second == 1:
        sec =f'{second} second'
    else : 
        sec =f'{second} seconds'
        
        
    if minutes == 0 : 
        min = ''
    elif minutes == 1 : 
        min =f'{minutes} minute'
    else :
        min =f'{minutes} minutes'
        
    if hours == 0 : 
        h = ''
    elif hours == 1:
        h =f'{hours} hour'
    else : 
         h =f'{hours} hours'
        
    if days == 0 : 
        d = ''
    elif days== 1:
        d =f'{days} day'
    else : 
        d =f'{days} days'
        
    if years == 0 : 
        y = ''
    elif years == 1:
        y =f'{years} year'
    else : 
        y =f'{years} years'
        
    list = [y, d, h , min , sec]
    
    final_list = []
    
    for el in list : 
        if el != '' :
            final_list.append(el) 
            
    answer = ''
            
    if len(final_list) == 1: 
        
        answer = final_list[0]
        
    elif len(final_list) == 2:
        answer = f'{final_list[0]} and {final_list[1]}'
        
    else:  
        first_part = ', '.join(final_list[:-1])
        answer = f'{first_part} and {final_list[-1]}'

    return answer 
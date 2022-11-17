def add_time(start_time, add_time, day=False):
    '''Adds time with an optional starting day
    Arguments:
    start_time: string
    add_time: string
    day: string

    Returns: The string of the added day and the days later.
    '''
    
    # Without Starting day
    if not day:

        # Splitting of the parameters:
        num_and_period = start_time.split()
        num = num_and_period[0]
        period = num_and_period[1]

        hour = int(num.split(':')[0])
        min = int(num.split(':')[1])

        add_hour = int(add_time.split(':')[0])
        add_min = int(add_time.split(':')[1])

        # Conditions for 12:00 AM and PM
        if period == 'PM':
            hour += 12
        elif period == 'AM' and hour == 12:
            hour = 0
            
        # For the total_min
        total_hour = hour + add_hour
        total_min = min + add_min

        # Condition for minute exceeding 60 mins / 1 hour
        if total_min >= 60:
            total_min -= 60
            total_hour += 1

        # For condition when less than 10
        if total_min < 10:
            total_min = '0'+ str(total_min)
        

        # For days added
        days_added = total_hour // 24

        # Related to period
        if (total_hour // 12) % 2 == 0: # Condition tells if it's in the AM
            total_hour = total_hour - (total_hour//12)*12
            if (total_hour % 24) == 0:
                total_hour = 12
            period = 'AM'
        else:
            total_hour = total_hour - (total_hour//12)*12
            if (total_hour % 12) == 0:
                total_hour = 12
            period = 'PM'
        
        if days_added == 0:
            new_time = f'{total_hour}:{total_min} {period}'
        elif days_added == 1:
            new_time = f'{total_hour}:{total_min} {period} (next day)'
        else:
            new_time = f'{total_hour}:{total_min} {period} ({days_added} days later)'

    # With starting day
    else:
        day = day.lower()

        day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        
        if day not in day_list:
            new_time = 'Starting day mispelled or incorrect.'

        day_index = day_list.index(day)

        # Splitting of the parameters:
        num_and_period = start_time.split()
        num = num_and_period[0]
        period = num_and_period[1]

        hour = int(num.split(':')[0])
        min = int(num.split(':')[1])

        add_hour = int(add_time.split(':')[0])
        add_min = int(add_time.split(':')[1])

        # Conditions for 12:00 AM and PM
        if period == 'PM':
            hour += 12
        elif period == 'AM' and hour == 12:
            hour = 0
        
        # For the total_min
        total_hour = hour + add_hour
        total_min = min + add_min

            # Condition for minute exceeding 60 mins / 1 hour
        if total_min >= 60:
            total_min -= 60
            total_hour += 1

        # For condition when less than 10
        if total_min < 10:
            total_min = '0'+ str(total_min)
        
        # For days added
        days_added = total_hour // 24
        days_added_remainder = days_added % 7 # Remove excess days
        if days_added == 0: # if there are no added days
            day = day.capitalize()
        else: # else if there are added days
            day_index += days_added_remainder
            if day_index >= 7:
                day_index = day_index - len(day_list)
            day = day_list[day_index]
            if days_added == 1: # For the next day
                day = f'{day.capitalize()} (next day)'
            else: # For n days later
                day = f'{day.capitalize()} ({days_added} days later)'

        # Related to period
        if (total_hour // 12) % 2 == 0:
            total_hour = total_hour - (total_hour//12)*12
            if (total_hour % 24) == 0:
                total_hour = 12
            period = 'AM'
        else:
            total_hour = total_hour - (total_hour//12)*12
            if (total_hour % 12) == 0:
                total_hour = 12
            period = 'PM'
            
        new_time = f'{total_hour}:{total_min} {period}, {day}'

    return new_time
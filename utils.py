def calculate_penalty(days_overdue):
    if days_overdue > 30:
        return days_overdue * 5
    elif days_overdue > 14:
        return days_overdue * 4
    elif days_overdue > 7:
        return days_overdue * 3.5
    elif days_overdue > 5:
        return days_overdue * 2
    else:
        return 0

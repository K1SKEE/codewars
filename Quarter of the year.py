'''Given a month as an integer from 1 to 12, return to which quarter of the year
it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is
part of the second quarter; and month 11 (November), is part of the fourth quarter.
'''


def quarter_of(month):
    if month > 0:
        if month > 3:
            if month > 6:
                if month > 9:
                    return 4
                return 3
            return 2
        return 1
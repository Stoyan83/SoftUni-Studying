# win_symbols = ('@', '#', '$', '^')
# win_patterns = [x * 6 for x in win_symbols]
# find_pattern = lambda x: next(filter(lambda y: y in x, win_patterns), None)
#
# tickets_list = input().split(',')
# tickets_list = [ticket.strip() for ticket in tickets_list if ticket.strip() != '']
#
# for ticket in tickets_list:
#     if len(ticket) != 20:
#         print('invalid ticket')
#     else:
#         pattern_found = find_pattern(ticket[:10])
#         if pattern_found and (pattern_found in ticket[10:]):  # winning ticket
#             pattern_char = pattern_found[0]
#
#             if ticket == pattern_char * 20:
#                 print(f'ticket "{ticket}" - 10{pattern_char} Jackpot!')
#
#             else:
#                 for i in range(10, 5, -1):
#                     if (pattern_char * i in ticket[:10]) and (pattern_char * i in ticket[10:]):
#                         print(f'ticket "{ticket}" - {i}{pattern_char}')
#                         break
#         else:
#             print(f'ticket "{ticket}" - no match')

def is_winning(ticket):
    if not len(ticket) == 20:
        return "invalid ticket"
    left_half = ticket[:10]
    right_half = ticket[10:]
    winning_chars = ['@', '#', '$', '^']
    for ch in winning_chars:
        for repetition in range(10, 5, -1):
            ch_repetition = ch * repetition
            if ch_repetition in left_half and ch_repetition in right_half:
                if repetition == 10:
                    return f'ticket "{ticket}" - {len(ch_repetition)}{ch} Jackpot!'
                elif 6 <= repetition <= 9:
                   return f'ticket "{ticket}" - {len(ch_repetition)}{ch}'
    return f'ticket "{ticket}" - no match'


tickets = [t.strip() for t in input().split(", ")]
tickets_state = []
for ticket in tickets:
    tickets_state.append(is_winning(ticket))

print(*tickets_state, sep="\n")


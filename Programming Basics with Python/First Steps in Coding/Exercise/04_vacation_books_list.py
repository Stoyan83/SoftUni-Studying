pages_in_current_book = int(input())
pages_read_per_hour = int(input())
days_to_read_book = int(input())

time_to_finish_book = pages_in_current_book / pages_read_per_hour
hours_needed_per_day = time_to_finish_book/ days_to_read_book

print(int(hours_needed_per_day))

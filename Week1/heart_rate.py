"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
user_age = int(input('enter your age: '))

maximum_heart_rate_per_min = 220 - user_age

max_exercise = 0.85 * maximum_heart_rate_per_min
min_exercise = 0.65 * maximum_heart_rate_per_min

print(f"When you exercise to strengthen your heart, you should"
      f"keep your heart rate between {min_exercise} and {max_exercise} beats per minute.")
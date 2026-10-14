import datetime, time
# datetime: is a module
print(datetime.date.today())
print(datetime.datetime.now())

# to print individual 
current_time = datetime.datetime.now()
print(current_time.day)
print(current_time.month)
print(current_time.year)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.microsecond)

# subtracting 2 dates in days
d1 = datetime.date(2000,8,11)
d2 = datetime.date(2026,9,3)
print(d2-d1)
print()

# subtracting 2 time in hrs
t1 = datetime.time(2,20,00)
print(t1)
print()


# to extract date after 15 days we will use timedelta()
today = datetime.date.today()
time_delta = datetime.timedelta(days=15)
print(today + time_delta)
print()

# creating own date and time object and print them individually
d_t = datetime.datetime(2022,4,20,2,30,50)
print(d_t)
print(d_t.date())
print(d_t.time())
print()

# strptime(): will convert string to datetime
sting_date1 = datetime.datetime.strptime('2022/06/25 02:30:50','%Y/%m/%d %H:%M:%S')
print(sting_date1)
sting_date2 = datetime.datetime.strptime('2022-06-25 02:30:50','%Y-%m-%d %H:%M:%S')
print(sting_date2)
print()

# strftime(): will convert datetime to string
date_string1 = datetime.datetime.strftime(datetime.datetime.today(), '%Y-%m-%d %H:%M:%S')
print(date_string1)
date_string2 = datetime.datetime.strftime(datetime.datetime.today(), '%Y/%m/%d %H:%M:%S')
print(date_string2)
print()

t = time.strftime('%Y-%m-%d %I-%M-%S%p',time.localtime())
print(t)
t1 = time.strftime("%Y-%m-%d", time.localtime())
print(t1)
print()

testtime = time.strftime("%I-%M-%S%p", time.localtime())
testdate = time.strftime("%Y-%m-%d", time.localtime())
print(testtime,testdate)


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. datetime.date vs datetime.time vs datetime.datetime - the object hierarchy
# -------------------------
# date       -> year, month, day only (no time component)
# time       -> hour, minute, second, microsecond only (no date component)
# datetime   -> combines BOTH date and time
# timedelta  -> represents a DURATION/DIFFERENCE, not a point in time

print(type(datetime.date.today()))       # <class 'datetime.date'>
print(type(datetime.datetime.now()))      # <class 'datetime.datetime'>
print(type(datetime.time(10, 30)))         # <class 'datetime.time'>
print(type(d2 - d1))                        # <class 'datetime.timedelta'>

print(f"{'*' * 60}")

# -------------------------
# 2. timedelta components - accessing days, seconds, and total_seconds()
# -------------------------
diff = d2 - d1
print(diff.days)              # total whole days in the difference
# print(diff.seconds)          # seconds component (0-86399), NOT total seconds!
print(diff.total_seconds())   # total difference expressed ENTIRELY in seconds (float)

# GOTCHA: timedelta.seconds is NOT the total seconds - it's the "leftover"
# seconds AFTER days are factored out. Always use total_seconds() if you want
# the full duration in seconds.
td = datetime.timedelta(days=1, hours=2, minutes=30)
print(td.days)              # 1
print(td.seconds)            # 9000  -> 2hr30min expressed in seconds, NOT including the 1 day
print(td.total_seconds())     # 95400.0 -> the FULL duration in seconds (86400 + 9000)

print(f"{'*' * 60}")

# -------------------------
# 3. Comparing dates/datetimes directly (no need to subtract first)
# -------------------------
print(d1 < d2)     # True -> date/datetime objects support direct comparison operators
print(d1 == d1)     # True

print(f"{'*' * 60}")

# -------------------------
# 4. weekday() vs isoweekday() - a classic "off by one" interview trap
# -------------------------
some_date = datetime.date(2026, 8, 21)   # a Friday
print(some_date.weekday())      # 4 -> Monday=0, Tuesday=1, ..., Sunday=6
print(some_date.isoweekday())    # 5 -> Monday=1, Tuesday=2, ..., Sunday=7 (ISO 8601 standard)

import calendar
print(calendar.day_name[some_date.weekday()])   # 'Friday' -> human-readable name

print(f"{'*' * 60}")

# -------------------------
# 5. isoformat() - the standard, unambiguous string representation
# -------------------------
now = datetime.datetime.now()
print(now.isoformat())    # '2026-08-21T10:15:30.123456' -> 'T' separates date and time (ISO 8601)
print(datetime.date.today().isoformat())   # '2026-08-21'

# isoformat() is generally PREFERRED over strftime() for machine-readable output
# (logging, APIs, storage) because it's unambiguous and has no locale dependency.

print(f"{'*' * 60}")

# -------------------------
# 6. Epoch / Unix timestamp conversions - VERY commonly asked
# -------------------------
# The "epoch" is January 1, 1970, 00:00:00 UTC - the reference point most
# systems use to represent time as a single number (seconds since epoch).
ts = time.time()
print(ts)                                     # e.g. 1755765330.123456 -> current time as a float

dt_from_ts = datetime.datetime.fromtimestamp(ts)
print(dt_from_ts)                               # converts epoch seconds -> local datetime

back_to_ts = dt_from_ts.timestamp()
print(back_to_ts)                                 # converts datetime -> epoch seconds (float)

# UTC-specific conversion (avoids local timezone ambiguity)
utc_dt = datetime.datetime.utcfromtimestamp(ts)     # deprecated since 3.12, shown for awareness
print(utc_dt)
# Preferred modern approach (Python 3.11+):
utc_dt_aware = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
print(utc_dt_aware)

print(f"{'*' * 60}")

# -------------------------
# 7. Naive vs Aware datetime objects - THE most important datetime concept
#    for real-world (production) code, and a frequent interview topic
# -------------------------
# NAIVE datetime: has no timezone info attached - Python has no idea if it's
# UTC, IST, EST, etc. Most of the examples above (datetime.now(), etc.) are NAIVE.
naive_dt = datetime.datetime.now()
print(naive_dt.tzinfo)     # None -> naive, no timezone attached

# AWARE datetime: has a timezone attached via tzinfo
aware_dt = datetime.datetime.now(datetime.timezone.utc)
print(aware_dt.tzinfo)      # datetime.timezone.utc -> aware

# GOTCHA: comparing a naive and an aware datetime raises a TypeError!
try:
    print(naive_dt < aware_dt)
except TypeError as e:
    print("Error:", e)   # can't compare offset-naive and offset-aware datetimes

# Best practice in real applications: ALWAYS store/compare datetimes in UTC
# (aware), and only convert to local time for DISPLAY purposes.

print(f"{'*' * 60}")

# -------------------------
# 8. Working with specific timezones - zoneinfo (Python 3.9+, built-in)
# -------------------------
from zoneinfo import ZoneInfo

utc_now = datetime.datetime.now(datetime.timezone.utc)
ist_now = utc_now.astimezone(ZoneInfo("Asia/Kolkata"))
print(utc_now)
print(ist_now)   # same instant, displayed in IST (UTC+5:30)

# NOTE: for Python < 3.9, the third-party 'pytz' library was traditionally
# used for this; zoneinfo is now the standard-library replacement.

print(f"{'*' * 60}")

# -------------------------
# 9. Common strftime/strptime format codes (quick-reference, frequently tested)
# -------------------------
# %Y -> 4-digit year (2026)      %y -> 2-digit year (26)
# %m -> month as zero-padded (08)  %B -> full month name (August)  %b -> abbreviated (Aug)
# %d -> day of month, zero-padded (21)
# %H -> 24-hour (00-23)            %I -> 12-hour (01-12)
# %M -> minute (00-59)             %S -> second (00-59)
# %p -> AM/PM
# %A -> full weekday name (Friday) %a -> abbreviated (Fri)
# %j -> day of year (001-366)
# %Z -> timezone name              %z -> UTC offset (+0000)

sample = datetime.datetime(2026, 8, 21, 14, 5, 9)
print(sample.strftime("%A, %B %d, %Y at %I:%M %p"))
# 'Friday, August 21, 2026 at 02:05 PM'

print(f"{'*' * 60}")

# -------------------------
# 10. Common error: strptime() format string MUST exactly match the input
# -------------------------
try:
    datetime.datetime.strptime("2026-08-21", "%Y/%m/%d")   # format uses '/' but string uses '-'
except ValueError as e:
    print("ValueError:", e)   # time data '2026-08-21' does not match format '%Y/%m/%d'

print(f"{'*' * 60}")

# -------------------------
# 11. time.sleep() and measuring elapsed time correctly
# -------------------------
start = time.perf_counter()    # best choice for measuring elapsed time (high-resolution, monotonic)
time.sleep(0.1)                  # pause execution for 0.1 seconds
elapsed = time.perf_counter() - start
print(f"Elapsed: {elapsed:.4f} seconds")

# NOTE: time.time() reflects WALL-CLOCK time and can jump backward/forward if
# the system clock is adjusted (e.g., NTP sync). time.perf_counter() is
# monotonic and specifically designed for measuring durations reliably.

print(f"{'*' * 60}")

# -------------------------
# 12. date.replace() - creating a modified copy (dates/datetimes are immutable!)
# -------------------------
d = datetime.date(2026, 8, 21)
d_new_year = d.replace(year=2027)
print(d)             # 2026-08-21 -> original unchanged
print(d_new_year)     # 2027-08-21 -> new object with only 'year' changed

# date/datetime/time/timedelta are all IMMUTABLE - just like int, str, tuple.
# You always get back a NEW object; there's no "in-place" modification.

print(f"{'*' * 60}")

# -------------------------
# 13. calendar module - useful utilities often paired with datetime
# -------------------------
print(calendar.isleap(2024))          # True  -> leap year check
print(calendar.isleap(2026))           # False
print(calendar.monthrange(2026, 2))     # (6, 28) -> (weekday of 1st day, number of days in month)


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON DATE & TIME HANDLING
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the difference between datetime.date, datetime.time,
#    datetime.datetime, and datetime.timedelta?
#
# 2. What is the difference between a "naive" and an "aware" datetime object?
#    Why does this distinction matter in production systems (e.g., a
#    multi-region web application)?
#
# 3. What happens if you try to compare a naive datetime with an aware
#    datetime? Why does Python raise this error instead of guessing?
#
# 4. What is the "epoch," and how would you convert a Unix timestamp to a
#    datetime object and back?
#
# 5. What is the difference between timedelta.seconds and
#    timedelta.total_seconds()? Why is this a common source of bugs?
#
# 6. What's the difference between date.weekday() and date.isoweekday()? Which
#    day does each consider "day 0" or "day 1"?
#
# 7. Why is datetime.isoformat() often preferred over strftime() for
#    logging or storing timestamps in a database or API payload?
#
# 8. How would you get the current time in a specific timezone (e.g.,
#    "Asia/Kolkata" or "America/New_York") using the standard library, without
#    installing pytz?
#
# 9. What's the difference between time.time() and time.perf_counter()? Which
#    one should you use to measure how long a piece of code took to run, and
#    why?
#
# 10. Are datetime objects mutable or immutable? How would you change just the
#     year of an existing date object without mutating the original?
#
# 11. What exception does strptime() raise if the input string doesn't match
#     the given format string, and what would trigger it?
#
# 12. What is the best practice for storing datetimes in a database or backend
#     system that serves users in multiple timezones? (Hint: think about when
#     to convert to local time.)
#
# 13. How would you check if a given year is a leap year using the standard
#     library, without writing the leap-year logic yourself?
#
# 14. What does datetime.timedelta represent, and how is it different from a
#     datetime or date object conceptually (a duration vs. a point in time)?
#
# 15. How would you add "1 month" to a date in Python? Why doesn't the
#     standard library's timedelta support a "months" argument directly, and
#     what would you use instead (hint: dateutil.relativedelta)?
#
# 16. What is the difference between datetime.now() and datetime.utcnow() (or
#     its modern replacement)? Why was utcnow() deprecated in recent Python
#     versions?
#
# 17. If two datetimes are equal in value but one is naive and one is aware
#     (in UTC, at the same moment), does Python consider them equal? Why or
#     why not?
#
# 18. How would you format a datetime into a human-readable string like
#     "Friday, August 21, 2026"? Which strftime format codes would you use?
#
# 19. What's the difference between %H and %I in strftime format codes? What
#     additional format code do you need if you use %I to avoid ambiguity?
#
# 20. Why might relying on time.sleep() for precise timing in a
#     performance-critical application be unreliable? What guarantees does it
#     NOT make?
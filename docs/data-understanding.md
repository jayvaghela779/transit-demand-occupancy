# data understanding

## initial inspection

file inspected: `od-2024-03-03.parquet`

the file has like 364,982 rows and 16 columns total. (pretty big file tbh)

ran the profiling script to check out column names, types, missing data, and duplicates. everything looks mostly normal.

## missing values

so only 77 rows have missing values out of hundreds of thousands. pretty small amount.

| column | missing values |
|---|---:|
| n-boardings | 77 |
| n-alighting | 73 |
| lag_loading | 73 |
| balance | 73 |
| loading | 77 |

yeah, so missing data is about 0.02% of the whole dataset. basically nothing, but still good to know it's there.

## route-wise distribution

figured out which routes are acting up:

| route | affected rows |
|---|---:|
| 22402 | 25 |
| 40302 | 21 |
| 164703 | 17 |
| 104602 | 14 |

## further investigation

looked deeper into the missing value combinations (used value_counts in pandas):

- 73 rows are missing all five passenger columns at once.
- 4 rows are just missing `n-boardings` and `loading`. (weird, need to check why)

turns out all these broken rows only belong to four specific trips in this file. 

oh, and zero duplicate rows found, which is nice.

## next things to check

- need to figure out why these specific passenger stats are missing (maybe device error on the bus?)
- check if this happens on other dates too or if it's just March 3rd.
- figure out if we should drop these rows or fill them with zeros / interpolate before we start training models.

note: remember this is just from ONE daily file!! don't draw any big conclusions for the whole historical dataset yet.
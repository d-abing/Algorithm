start_time = (input().split())[::2]
end_time = (input().split())[::2]

st = list(map(int, start_time))
et = list(map(int, end_time))

def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

st_seconds = time_to_seconds(*st)
et_seconds = time_to_seconds(*et)

diff_seconds = et_seconds - st_seconds

if diff_seconds < 0:
    diff_seconds += 24 * 3600

print(diff_seconds)
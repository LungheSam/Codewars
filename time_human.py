from math import floor,ceil

def make_readable(seconds):
    HH=seconds/3600
    MM=(HH - floor(HH))*60
    SS=(MM -floor(MM))*60
    # print(HH,MM,SS)
    HH=floor(HH)
    MM=floor(MM)
    if "59" in str(SS):
        SS=59
    else:
        SS=round(SS)
    if HH<10:
        HH="0"+str(HH)
    if MM<10:
        MM="0"+str(MM)
    if SS<10:
        SS="0"+str(SS)
    time_human=f"{HH}:{MM}:{SS}"
    # print(time_human)
    return time_human

make_readable( 182006)

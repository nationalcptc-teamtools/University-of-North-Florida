# OSI
### level 2 
- Look up each code online and find the cars
### level 3
- file name is a hash use MD5 hash decoder: porttarget
- binwalk 75800450385424f98f64c36fa4d40fb20b26f5e9.png 
    - tells there is zlib compressed data
# log analysis
### level 1
- `cat access.log | cut -d " " -f 1 | sort | uniq | wc -l` 100 IP are connected
- `egrep access.log | wc -l access.log` // 394 requests in access log
- `cat access.log | cut -d '"' -f 3 | cut -d ' ' -f 2 | sort | uniq -c | sort -rn`  175 200 status codes
- `awk '{ if($9 == 404) { print $7 } }' access.log │ | sort | uniq -c | sort -nr | head -10  `   /.env had 35 404 requests
-  `awk '{print $1}' access.log | sort -n | uniq -c | sort -nr > web.txt` ip 212.47.65.231 made 46 requests
### level 2
- `egrep activity.log | wc -l activity.log` 56975
- `awk '{print $1, $NF}' /path/to/eventlog.log | sort -k 1 | uniq -c | sort -rn | head -1` 2024-04-17 date the most events occurred Earnestine.Hettingter49
- `grep -oP '"timestamp":"\K\d{4}-\d{2}-\d{2}' activity.log | sort | uniq | wc -l` 173 unique calendar dates
# Airflow Automation
- make sure you copy your airflow scheduler (`emoji_metrics_scheduler.py`) to `/path/to/airflow/dags` location
- check out [this](https://youtu.be/Yjk2m--ot-w) video to see how I did it

## Result
Here's the result. So far, not many emojies, but it should go up as I collect more tweets

```bash
$ psql -c 'select * from numberofemojis order by number_emojis desc limit 10;' 'postgresql://<user>:<pass>@localhost:5432/tweets'
         id          | number_emojis
---------------------+---------------
 1309986791513038848 |             1
 1310956934275698689 |             1
 1310949042579439624 |             1
 1311018379172552715 |             0
 1310992358142603266 |             0
 1310989847780364290 |             0
 1310998056305856513 |             0
 1310967128783302658 |             0
 1310962808117493761 |             0
 1310968071042068481 |             0
(10 rows)
```

#Задание 2
scooter_rent=# SELECT "track",
scooter_rent-# CASE
scooter_rent-# WHEN "finished" = true THEN 2
scooter_rent-# WHEN "cancelled" = true THEN -1
scooter_rent-# WHEN "inDelivery" = true THEN 1
scooter_rent-# ELSE 0
scooter_rent-# END as status
scooter_rent-# FROM "Orders";
 track  | status
--------+--------
 239337 |      2
 239337 |      2
 527071 |      2
 527071 |      2
 313725 |      2
 313725 |      2
 406421 |      1
 406421 |      1
 980012 |      1
 980012 |      1
 737863 |      1
 737863 |      1
 268954 |      1
 268954 |      1
(14 rows)
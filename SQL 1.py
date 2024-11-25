#Задание 1
scooter_rent=# SELECT "Couriers"."login", COUNT(*)
scooter_rent-# FROM "Orders"
scooter_rent-# JOIN "Couriers" ON "Orders"."courierId" = "Couriers"."id"
scooter_rent-# WHERE "Orders"."inDelivery" = true
scooter_rent-# GROUP BY "Couriers"."login";
 login  | count
--------+-------
 dima   |     8
 nikita |     2
 oleg   |     4
(3 rows)

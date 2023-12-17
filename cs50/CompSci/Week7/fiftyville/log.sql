-- Keep a log of any SQL queries you execute as you solve the mystery.
-- View indexes in DB (there are none). We'll add as needed if queries get slow
SELECT type, name, tbl_name, sql 
  FROM sqlite_master 
 WHERE type= 'index';

-- Find crime scene reports for the date and street (7/28/2021, Humphrey Street)
SELECT id, description
  FROM crime_scene_reports
 WHERE year = 2021 
    AND month = 7 
    AND day = 28
    AND street LIKE '%Humphrey%';

-- 295|Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
-- Get the interviews related to the crime scene report
SELECT id, name, transcript
  FROM interviews
 WHERE year = 2021
    AND month = 7
    AND day = 28
    AND transcript LIKE '%bakery%';

-- 161|Ruth|Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
SELECT id, activity, license_plate, hour, minute
  FROM bakery_security_logs
 WHERE year = 2021
    AND month = 7
    AND day = 28
    and hour = 10
    and minute between 15 and 25;

/* Cars that left the bakery within 10 minutes of crime
260|exit|5P2BI95|10|16
261|exit|94KL13X|10|18
262|exit|6P58WS2|10|18
263|exit|4328GD8|10|19
264|exit|G412CB7|10|20
265|exit|L93JTIZ|10|21
266|exit|322W7JE|10|23
267|exit|0NTHK55|10|23
*/    

-- 162|Eugene|I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
SELECT t.account_number, t.atm_location, t.transaction_type, t.amount,
       a.person_id, a.creation_year,
       p.name, p.phone_number, p.passport_number, p.license_plate
  FROM atm_transactions t
  JOIN bank_accounts a ON a.account_number = t.account_number
  JOIN people p ON p.id = a.person_id
 WHERE t.year = 2021
    AND t.month = 7
    AND t.day = 28
    AND t.atm_location like '%Legget%'
    AND t.transaction_type = 'withdraw';

/*
49610011|Leggett Street|withdraw|50|686048|2010|Bruce|(367) 555-5533|5773159633|94KL13X -> 261|exit|94KL13X|10|18
26013199|Leggett Street|withdraw|35|514354|2012|Diana|(770) 555-1861|3592750733|322W7JE -> 266|exit|322W7JE|10|23
16153065|Leggett Street|withdraw|80|458378|2012|Brooke|(122) 555-4581|4408372428|QX4YZN3
28296815|Leggett Street|withdraw|20|395717|2014|Kenny|(826) 555-1652|9878712108|30G67EN
25506511|Leggett Street|withdraw|20|396669|2014|Iman|(829) 555-5269|7049073643|L93JTIZ -> 265|exit|L93JTIZ|10|21
28500762|Leggett Street|withdraw|48|467400|2014|Luca|(389) 555-5198|8496433585|4328GD8 -> 263|exit|4328GD8|10|19
76054385|Leggett Street|withdraw|60|449774|2015|Taylor|(286) 555-6063|1988161715|1106N58
81061156|Leggett Street|withdraw|30|438727|2018|Benista|(338) 555-6650|9586786673|8X428L0

The thief is one of the 4 identified above as having left in a car from the bakery within 10 minutes of the theft.
*/

-- 163|Raymond|As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. 
-- The thief then asked the person on the other end of the phone to purchase the flight ticket.
SELECT id, duration, caller, receiver
  FROM phone_calls
 WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60; -- duration appears to be in seconds

/*
221|51|(130) 555-0289|(996) 555-8899
224|36|(499) 555-9472|(892) 555-8872
233|45|(367) 555-5533|(375) 555-8161
251|50|(499) 555-9472|(717) 555-1342
254|43|(286) 555-6063|(676) 555-6554
255|49|(770) 555-1861|(725) 555-3243
261|38|(031) 555-6622|(910) 555-3251
279|55|(826) 555-1652|(066) 555-9701
281|54|(338) 555-6650|(704) 555-2131

These are the two remaining suspects. They both left the bakery within 10 minutes of the theft and made a call that was under 1 minute. Additionally,
the recipient of the call is the accomplice.
49610011|Leggett Street|withdraw|50|686048|2010|Bruce|(367) 555-5533|5773159633|94KL13X -> 261|exit|94KL13X|10|18 -> 233|45|(367) 555-5533|(375) 555-8161
26013199|Leggett Street|withdraw|35|514354|2012|Diana|(770) 555-1861|3592750733|322W7JE -> 266|exit|322W7JE|10|23 -> 255|49|(770) 555-1861|(725) 555-3243
*/

-- find the earliest flight out of Fiftyville on 7/29/2021
SELECT f.id as flight_id, f.hour, f.minute,
       a.abbreviation, a.full_name, a.city
  FROM flights f 
  JOIN airports a ON a.id = f.origin_airport_id
 WHERE a.city = 'Fiftyville'
    AND f.year = 2021
    AND f.month = 7
    AND f.day = 29
ORDER BY hour, minute ASC
LIMIT 1;

/*
This is the earliest flight for the next day out of Fiftyville
36|8|20|CSF|Fiftyville Regional Airport|Fiftyville

Did phone number (375) 555-8161 or (725) 555-3243 book this flight?
*/
-- get the passengers on the flight
SELECT p1.flight_id, p1.passport_number, p1.seat,
       p2.name, p2.phone_number, p2.license_plate
  FROM passengers p1 
  JOIN people p2 ON p2.passport_number = p1.passport_number
 WHERE flight_id = 36;

/*
36|7214083635|2A|Doris|(066) 555-9701|M51FA04
36|1695452385|3B|Sofia|(130) 555-0289|G412CB7
36|5773159633|4A|Bruce|(367) 555-5533|94KL13X <-- The only one of the two remaining suspects on the flight. Gotcha!
36|1540955065|5C|Edward|(328) 555-1152|130LD9Z
36|8294398571|6C|Kelsey|(499) 555-9472|0NTHK55
36|1988161715|6D|Taylor|(286) 555-6063|1106N58
36|9878712108|7A|Kenny|(826) 555-1652|30G67EN
36|8496433585|7B|Luca|(389) 555-5198|4328GD8
*/

-- Get the accomplice. (375) 555-8161 is the number Bruce called.
SELECT id, name
  FROM people
 WHERE phone_number = '(375) 555-8161';

-- 864400|Robin <-- accomplice

-- Get the destination city
SELECT a.city
  FROM flights f 
  JOIN airports a ON a.id = f.destination_airport_id
 WHERE f.id = 36;
 

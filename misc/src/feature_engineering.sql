-- Behavioral Similarity Matrix

/*
Feature: Total number of calls/texts made by user by hour blocks
 */

CREATE MATERIALIZED VIEW vw_user_call_sms_hour_block
  AS
SELECT
case when hour_of_day < 9 then
  '00-09'
  when hour_of_day between 9 and 18 then
    '09-17'
  else
    '17-00'
End hour_block, sub.userid, sum(count_calls) calls_sms_count
from
(select userid, count(*) count_calls,  date_part('hour', startts) hour_of_day
from events
where eventtype in (6,7)
GROUP BY 1,3) sub
GROUP BY 1,2
ORDER BY userid, hour_block;


/*

 */

/******************************
  Mobility Similarity Matrix
 ******************************/

/*
  freq of updates by User by cell lifetime
 */
CREATE MATERIALIZED VIEW vw_1000cell_user_freq_lifetime
AS
  SELECT
    c.cellid,
    e.userid,
    count(*) freq_updates
  FROM (SELECT
          startcellid,
          userid
        FROM events
        WHERE eventtype = 1) e
    INNER JOIN cells c
      ON c.cellid = e.startcellid
    INNER JOIN vw_top1000_cells vt
      ON c.cellid = vt.startcellid
  GROUP BY c.cellid, e.userid
  ORDER BY e.userid, freq_updates DESC;


-- *** Loading Pivoted Data of vw_1000cell_user_freq_lifetime




/*
  Average network events at distinct cells per day for each user.
  This tells us the how mobile the user is.
  that is, it shows how much area the user covers on an average day
 */
CREATE MATERIALIZED VIEW vw_avg_event_by_distinct_cell
  AS
SELECT
  round(avg(updates_per_day)) avg_updates_per_day,
  userid
FROM
  (SELECT
     count(DISTINCT startcellid) updates_per_day,
     userid,
     startts :: DATE
   FROM events
   WHERE eventtype IN (1, 5, 6, 7)
   GROUP BY 2, 3
   ORDER BY userid) update_events_count
GROUP BY 2;

--######### Helper Queries #########
/*
  Location updates by hour of day by cell
 */
select count(*)
from(
SELECT
  count(*)                                                                                     cell_count,
  userid,
  e.startcellid :: CHARACTER VARYING || '_h_' || date_part('hour', e.startts) :: CHARACTER VARYING antenna_by_hour
FROM events e LEFT JOIN vw_top1000_cells vt
  ON e.startcellid = vt.startcellid
GROUP BY 3,2
HAVING count(*) > 5) ant;


/*
100 Antennas with most distinct users
 */
CREATE VIEW vw_top1000_cells
  AS
SELECT count(DISTINCT userid) user_count, startcellid
from events
GROUP BY startcellid
ORDER BY user_count desc limit 3000;







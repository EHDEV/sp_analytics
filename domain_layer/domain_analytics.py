from data_access_layer.dao import Dao
import json

class domain_analytics:

    def __init__(self):

        self.dao = Dao()

    def user_activity_hourly(self, user_id):
        """

        :type kwargs: object
        """

        q = '''
            SELECT count(*) freq, date_part('hour', e.startts) hour_of_day
            FROM events e
            WHERE eventtype in (5,6,7)
                  --AND e.userid = '{}'
            GROUP BY
              hour_of_day
            ORDER BY hour_of_day, freq DESC;        '''.format(user_id)

        data = self.dao.query(q)
        return data

    def traffic_weekday(self):
        q = '''
            select case when trim(a.day_of_week) = 'monday' then 1
          when trim(a.day_of_week) = 'tuesday' then 2
          when trim(a.day_of_week) = 'wednesday' then 3
          when trim(a.day_of_week) = 'thursday' then 4
          when trim(a.day_of_week) = 'friday' then 5
          when trim(a.day_of_week) = 'saturday' then 6
          when trim(a.day_of_week) = 'sunday' then  7 END day_num, *, a.day_of_week
          FROM (
            SELECT
              count(*)                  freq,
              to_char(e.startts, 'day') day_of_week
            FROM events e
            WHERE eventtype IN (5, 6, 7)
            --AND e.userid = '{}'
            GROUP BY
              2
          ) a
        ORDER BY day_num
        '''

        data = self.dao.query(q)
        return data


    def user_location_hourly(self, user_id, start_ts='', end_ts=''):
        params = dict(userid=user_id, starts=start_ts, end_ts=end_ts)
        tmp_whr = "WHERE e.eventtype = 1 AND "
        whr = construct_where_clause(params, whr=whr)
        q = '''SELECT DISTINCT c.cellid, c.longitude, c.latitude, date_part('hour', e.startts) hour_of_day
          FROM events e
            INNER JOIN cells c
              ON e.startcellid = c.cellid
          WHERE e.userid = '{}'
                and e.startts > '{}'
                and e.startts < '{}'
                and e.eventtype = 1
          GROUP BY hour_of_day, c.cellid, c.longitude, c.latitude
          ORDER BY hour_of_day;'''.format(user_id)

        data = dao.query(q)
        return data

    def construct_where_clause(self, params, whr='WHERE '):

        w_clause = whr
        for k in params:
            if params[k] == '' or params[k] == None:
                continue
            else:
                w_clause += "{} = {} AND ".format(k, params[k])

        w_clause.replace(" AND ", "")

        return w_clause

    def get_desc_stats(self):

        data_list = []

        q = '''select count(DISTINCT userid) active_users from events;'''

        data_list += self.dao.query(q)

        # q = '''select count(DISTINCT startcellid) active_cells from events;'''
        #
        # data_list += self.dao.query(q)

        q = '''select count(DISTINCT userid) call_text_events from events where eventtype in (5,6,7);'''

        data_list += self.dao.query(q)

        q = '''select count(DISTINCT userid) total_unique_amenities from events;'''

        data_list += self.dao.query(q)

        return data_list


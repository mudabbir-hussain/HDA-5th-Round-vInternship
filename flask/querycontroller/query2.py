from dbconnection.dbcon import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query2 = "SELECT s.name, SUM(t.total_price) " \
                 "FROM ecomdb_star_schema.fact_table t " \
                 "JOIN ecomdb_star_schema.customer_dim s on s.customer_key=t.customer_key " \
                 "JOIN ecomdb_star_schema.trans_dim tim on tim.payment_key=t.payment_key " \
                 "GROUP BY CUBE (s.name) " \
                 "ORDER BY s.name"
        cur.execute(query2)
        result = cur.fetchall()[:10]
        pd_data = pd.DataFrame(list(result), columns=['name', 'sales'])
        # pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q2 = Query2()
    data = q2.execute()
    print(data)
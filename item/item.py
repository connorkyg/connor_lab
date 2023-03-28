# -*- coding: utf-8 -*-
import psycopg2
import json

import tmp


class connect:
    conn = psycopg2.connect(
        host="192.168.1.126",
        database="testdb",
        user="test",
        password="ssrinc!123",
        port="5432"
    )

    for item_code in tmp.itemlist:
        with conn.cursor() as cur:
            cur.execute(f"SELECT item_alternative FROM item where item_code similar to ('{item_code}') limit 1;")
            a = cur.fetchone()[0]
            if a is None:
                pass
            else:
                print(item_code, a)
            conn.commit()

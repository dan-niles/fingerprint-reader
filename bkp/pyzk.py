# -*- coding: utf-8 -*-
from zk import ZK
import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)


conn = None
zk = ZK('172.21.0.8', port=4370)
print(zk)
try:
    conn = zk.connect()
    users = conn.get_users()
    for attendance in conn.live_capture():
        if attendance is None:
            pass
        else:
            user_data = str(attendance).split()
            for user in users:
                if user.user_id == user_data[1]:
                    template = conn.get_user_template(uid=user.uid, temp_id=6)
                    print(user)
                    print(template)
                    # print('+ UID #{}'.format(user.uid))
                    # print('  Name      : {}'.format(user.name))
                    # print('  User ID   : {}'.format(user.user_id))

except Exception as e:
    print("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()

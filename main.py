from os.path import expanduser

import pandas as pd
import paramiko
import pymysql
from sshtunnel import SSHTunnelForwarder


def execute_query():
    home = expanduser('~')
    mypkey = paramiko.RSAKey.from_private_key_file("/Users/santanu/.ssh/id_rsa")
    # if you want to use ssh password use - ssh_password='your ssh password', bellow

    sql_hostname = 'ula-prd-mysql-cluster-yoda.cluster-cvpukdkik4sz.ap-southeast-1.rds.amazonaws.com'
    sql_username = 'santanu.naskar@ula.app'
    sql_password = 'tJrcG7I9S5XNh580'
    sql_main_database = 'yoda_db'
    sql_port = 3306
    ssh_host = 'bastion.ula.app'
    ssh_user = 'santanu-naskar'
    ssh_port = 22

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=mypkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host="127.0.0.1", user=sql_username,
                               passwd=sql_password, db=sql_main_database,
                               port=tunnel.local_bind_port)
        query = '''SELECT VERSION();'''
        data = pd.read_sql_query(query, conn)
        print(data)
        conn.close()

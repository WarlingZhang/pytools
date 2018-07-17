addrs = ["10.100.244.43",
         "10.100.244.46",
         "10.100.244.51",
         "10.100.244.63",
         "10.100.244.64",
         "10.100.244.67",
         "10.100.244.68",
         "10.100.244.75"]
username = "jdcsjsb"
sumIndex = 1
for i in range(len(addrs)):
    addr = addrs[i]
    # seq = i + 1
    len2 = 6
    if i >= 3:
        len2 = 5
    for j in range(len2):
        sumIndexStr = str(sumIndex)
        sumIndexStr = sumIndexStr.zfill(2)
        username1 = username+sumIndexStr
#         text = """<dataHost name="%s" maxCon="1000" minCon="10" balance="0"
#             writeType="0" dbType="oracle" dbDriver="jdbc" switchType="1"  slaveThreshold="100">
#
#     <heartbeat>SELECT 1 from DUAL</heartbeat>
#     <connectionInitSql>alter session set nls_date_format='YYYY-MM-DD HH24:MI:SS'</connectionInitSql>
#     <writeHost host="%s" url="jdbc:oracle:thin:@%s:1521:orcl" user="%s"
#                 password="%s">
#     </writeHost>
#
# </dataHost>
# """
#         text = text % (username1, username1, addr, username1, username)
#         text = "<dataNode name=\"dn"+str(sumIndex)+"\" dataHost=\""+username1+"\" database=\""+username1+"\" />"

        text = """echo start%s
sqlplus %s/jdcsjsb@%s/orcl @建表语句.sql
echo end%s"""
        text = text % (username1, username1, addr, username1)
        print(text)
        sumIndex += 1

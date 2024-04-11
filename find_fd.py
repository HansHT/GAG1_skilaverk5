#from itertools import permutations

SQLquery = """
SELECT 'Boats: %s --> %s' AS FD,
CASE WHEN COUNT(*)=0 THEN 'MAY HOLD'
ELSE 'does not hold' END AS VALIDITY
FROM (
    SELECT X.%s
    FROM Boats X
    GROUP BY X.%s
    HAVING COUNT(DISTINCT X.%s) > 1
);
"""

def PrintSQL(Att1, Att2):
    print(SQLquery % (Att1, Att2, Att1, Att1, Att2))

#R = ['ID', 'PID', 'SID', 'SN', 'PN', 'MID', 'MN']
#R = ['UID', 'UN', 'SID', 'TI', 'RA', 'IMDB', 'S']
#R = ['PID', 'HID', 'PN', 'S', 'HS', 'HZ', 'HC']
#R = ['MID', 'D', 'HID', 'HN', 'AID', 'AN', 'RID', 'RN', 'H', 'A']
R = ['BL', 'BNo', 'Z', 'T', 'BN', 'SSN']

for i in range(len(R)):
    for j in range(len(R)):
        if (i != j):
            PrintSQL(R[i], R[j])


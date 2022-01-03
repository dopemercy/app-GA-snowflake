USERNAME = "dopemercy"
PASSWORD = "Dopemercy@123"
ACCOUNT = "mr86286.us-east-2.aws"
WAREHOUSE='COMPUTE_WH'
DATABASE="GOOGLE_ANALYTICS"

import snowflake.connector as sf
sf.paramstyle = 'qmark'
sfConnection=sf.connect(
		user=USERNAME,
		password=PASSWORD,
		account=ACCOUNT,
		warehous=WAREHOUSE,
		database=DATABASE,
	)

cursor=sfConnection.cursor()

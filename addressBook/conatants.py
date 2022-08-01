DB_PATH = 'DB/'

Create_Table_Query = "Create Table if not exists Address (LONGITUDE  INT NOT NULL, LATTITUDE  INT NOT NULL)"
Delete_Query = "delete from Address where LONGITUDE is ? and LATTITUDE is ?"
Insert_Query = "insert into Address (LONGITUDE, LATTITUDE)  values (?,?)"
Update_Query = "update Address set LONGITUDE = ? , LATTITUDE = ? where LONGITUDE=? and LATTITUDE=?"
Fetch_Query = 'select * from Address'

import datetime

today = datetime.date.today() 
# ↑　date型のメソッド　today =　今日の日付
birthday = datetime.date(1993,11,4)
# ↑　date型は0000年00月00日0時0分0秒まで表せることができる
life = today - birthday 
# ↑　今日の日付から生まれた日にちを引く
print(life.days)

# kakikukeko
#coding:utf-8
import xlrd
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","qdjfsyslog.settings")

if django.VERSION >= (1, 7):
    django.setup()

def main():
    from syslog.models import Serverslog
    bk = xlrd.open_workbook('1.xls')
    sh = bk.sheet_by_name('Sheet1')
    nrows = sh.nrows
    count = 0
    for i in range(nrows):
        s_date = sh.cell_value(i, 0)
        s_date = xlrd.xldate_as_tuple(s_date,0)
        s_date = str(s_date[0]) + '-' + str(s_date[1]) + '-' + str(s_date[2])
        s_time = sh.cell_value(i, 1)
        s_time = xlrd.xldate_as_tuple(s_time,0)
        s_time = str(s_time[3]) + ':' + str(s_time[4])
        calltimes = int(sh.cell_value(i, 2))
        s_name = sh.cell_value(i, 3)
        tel = str(sh.cell_value(i, 4))[0:11]
        questions_type = sh.cell_value(i, 5)
        s_body = sh.cell_value(i, 6)
        answer_status = int(sh.cell_value(i, 7))
        #Serverslog.objects.get_or_create(s_date=s_date, s_time=s_time, calltimes=calltimes, s_name=s_name, tel=tel, questions_type=questions_type, s_body=s_body, answer_status=answer_status)
        if count > 9:
            break
        count += 1
if __name__ == "__main__":
    main()
    print ('done!')


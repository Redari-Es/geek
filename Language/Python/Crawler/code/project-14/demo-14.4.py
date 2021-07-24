import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('Python', cell_overwrite_ok=True)

alignment = xlwt.Alignment()
#
alignment.horz = xlwt.Alignment.HORZ_CENTER
#
alignment.vert = xlwt.Alignment.VERT_CENTER
style = xlwt.XFStyle()
style.alignment = alignment

ws.write_merge(0, 0, 0, 5, 'Python网络爬虫', style)

for i in range(2, 7):
    for k in range(5):
        ws.write(i, k, i + k)
    ws.write(i, 5,
             xlwt.Formula('SUM(A' + str(i + 1) + ':E' + str(i + 1) + ')'))

#ws.insert_bitmap('test.bmp', 9, 1, 2, 2, scale_x=0.3, scale_y=0.3)
wb.save('file.xls')

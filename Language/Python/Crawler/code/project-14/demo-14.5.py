import xlrd

wb = xlrd.open_workbook('file.xls')
#
ws_count = wb.nsheets
print('Sheets总数：', ws_count)
#
#
#
#
ws = wb.sheet_by_name('Python')
#
row_value = ws.row_values(3)
print('第4行数据:', row_value)
#
row_col = ws.col_values(3)
print('D列数据：', row_col)

#
nrows = ws.nrows
ncols = ws.ncols
print('总行数：', nrows, ',总列数：', ncols)

#
cell_F3 = ws.cell(2, 5).value
print('F3内容：', cell_F3)

#
row_F3 = ws.row(2)[5].value
col_F3 = ws.row(5)[2].value
print('F3内容:', row_F3, 'F3内容:', col_F3)

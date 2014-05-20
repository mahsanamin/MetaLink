#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

fname = '../unit_stats.xlsx'
book = xlrd.open_workbook(fname)
sheet = book.sheet_by_name('Fusion_Stats')

# --------------------------------------------------
#print sheet.nrows
#print sheet.ncols

# --------------------------------------------------
ID_IDX = 0
HP_FUSION_IDX = 1
ATK_FUSION_IDX = 2
REC_FUSION_IDX = 3
DEF_FUSION_IDX = 4

# --------------------------------------------------
field_name_dict = {
    ID_IDX: 'id | (int)',
    HP_FUSION_IDX: 'hp_fusion | hpf(int)',
    ATK_FUSION_IDX: 'atk_fusion | atkf (int)',
    REC_FUSION_IDX: 'rec_fusion | recf (int)',
    DEF_FUSION_IDX: 'def_fusion | deff (int)',
}
# ---------------------------------------------
bool_str_to_int_dict = {
    'Y': 1,
    'YES': 1,
    'T': 1,
    'TRUE': 1,
    '1': 1,

    'N': 0,
    'NO': 0,
    'F': 0,
    'FALSE': 0,
    '0': 0,
}
# ---------------------------------------------
start_row = 2
start_col = 0
# --------------------------------------------------
# display title fields
#row = 36
#rec = []
#for col in xrange(start_col, sheet.ncols):
    #val = sheet.cell_value(row, col)
    #if len(val) <= 0:
        #rec.append(sheet.cell_value(row+1, col))
    #rec.append(val)
#print ",".join(map(str, rec))

# --------------------------------------------------
def load_dict_from_sheet(workbook, sheet_name):
    sheet = workbook.sheet_by_name(sheet_name)
    start_col = 0
    start_row = 2
    result_dict = {}
    for row in xrange(start_row, sheet.nrows):
        id = sheet.cell_value(row, 0)
        name = sheet.cell_value(row, 1)
        result_dict[name.upper()] = id
    return result_dict
# --------------------------------------------------
#element_mods_dict = load_dict_from_sheet(book, 'Element_Mods')
#unit_growth_dict = load_dict_from_sheet(book, 'Unit_Growth')
#class_type_dict = load_dict_from_sheet(book, 'Class_Type')
#attack_type_dict = load_dict_from_sheet(book, 'Attack_Type')
# --------------------------------------------------

# parse to .csv file from excel file.
field_list = tuple(sorted(field_name_dict.keys()))

# field_name
s = ''
for col in field_list:
    s += "%s," % field_name_dict[col]
print s

# data
for row in xrange(start_row, sheet.nrows):
    rec = []
    for col in field_list:
        if sheet.cell_type(row, col) == xlrd.XL_CELL_TEXT:
            val = '"' + sheet.cell_value(row, col) + '"'
        elif sheet.cell_type(row, col) == xlrd.XL_CELL_NUMBER:
            val = int(sheet.cell_value(row, col))
        else:
            val = sheet.cell_value(row, col)
        #if col == UNIT_ELEMENT_IDX:
            #try:
                #val = element_mods_dict[val.upper()]
            #except BaseException, e:
                #val = 0

        #print "row: %d, col:%d :%s" % (row, col, val)
        rec.append(val)

    print u",".join(map(unicode, rec)).encode('utf8')

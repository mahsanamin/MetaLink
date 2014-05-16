#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

fname = '../level_stats.xlsx'
book = xlrd.open_workbook(fname)
sheet = book.sheet_by_name('Level Design')

# --------------------------------------------------
#print sheet.nrows
#print sheet.ncols

# --------------------------------------------------
ID_IDX = 1
LOCATION_ID_IDX = 2
PARENT_ZONE_ID_IDX = 3
LEVEL_ID_IDX = 4
NODE_ID_IDX = 5
PARENT_ZONE_IDX = 6
LEVEL_NODE_IDX = 7
STAGE_NAME_IDX = 8
DESCRIPTION_IDX = 9
STAGE_DIALOGUE_GROUP_ID_IDX = 10
EXP_IDX = 11
MONEY_IDX = 12
COST_STAMINA_IDX = 13
MAX_BATTLEWAVE_COUNT_IDX = 14
MAX_MOBS_BATTLEWAVE_IDX = 15
NORMAL_MOB_GROUP_ID_IDX = 16
MOB_LEVEL_DIFFICULTY_IDX = 17
FINAL_BOSS_GROUP_ID_IDX = 18
BOSS_LEVEL_DIFFICULTY_IDX = 19
DUNGEON_LEVEL_VARIABLES_IDX = 20
SPECIAL_BONUS_STAGE_GROUP_ID_IDX = 21
SPECIAL_BONUS_STAGE_IDX = 22
LOOT_ID_IDX = 23

# --------------------------------------------------
field_name_dict = {
    ID_IDX: 'id | (int)',
    LOCATION_ID_IDX: 'location_id | locid (int)',
    PARENT_ZONE_ID_IDX: 'parent_zone_id | pzid (int)',
    LEVEL_ID_IDX: 'level_id | lvid (int)',
    NODE_ID_IDX: 'node_id | nid (int)',
    PARENT_ZONE_IDX: 'parent_zone | pz (string)',
    LEVEL_NODE_IDX: 'level_node | ln (string)',
    STAGE_NAME_IDX: 'stage_name | sn (string)',
    DESCRIPTION_IDX: 'description | desc (string)',
    STAGE_DIALOGUE_GROUP_ID_IDX: 'stage_dialogue_group_id | sdgi (int)',
    EXP_IDX: 'exp | exp (int)',
    MONEY_IDX: 'money | money (int)',
    COST_STAMINA_IDX: 'cost_stamina | cs (int)',
    MAX_BATTLEWAVE_COUNT_IDX: 'max_battlewave_count | mbc (int)',
    MAX_MOBS_BATTLEWAVE_IDX: 'max_mobs_battlewave | mbbl (int)',
    NORMAL_MOB_GROUP_ID_IDX: 'normal_mob_group_id | nmgi (int)',
    MOB_LEVEL_DIFFICULTY_IDX: 'mob_level_difficulty | mld (string)',
    FINAL_BOSS_GROUP_ID_IDX: 'final_boss_group_id | fbgi (int)',
    BOSS_LEVEL_DIFFICULTY_IDX: 'boss_level_difficulty | bld (string)',
    DUNGEON_LEVEL_VARIABLES_IDX: 'dungeon_level_variables | dlv (int)',
    SPECIAL_BONUS_STAGE_GROUP_ID_IDX: 'special_bonus_stage_group_id | sbsg (int)',
    SPECIAL_BONUS_STAGE_IDX: 'special_bonus_stage | sbs (string)',
    LOOT_ID_IDX: 'loot_id | loi (int)',
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
start_row = 1
start_col = 1
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


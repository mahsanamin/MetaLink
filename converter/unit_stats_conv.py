#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

fname = '../unit_stats.xlsx'
book = xlrd.open_workbook(fname)
sheet = book.sheet_by_name('UNIT DATA')

# --------------------------------------------------
#print sheet.nrows
#print sheet.ncols

# --------------------------------------------------
ID_IDX = 1
ARCHTYPE_NAMEING_IDX = 2
UNIT_NAME_IDX = 6
NEXT_EVOLVE_IDX = 7
UNIT_ELEMENT_IDX = 8
MAX_LV_IDX = 9
EXP_MOD_IDX = 10
UNIT_GROWTH_IDX = 11
RARITY_TIER_IDX = 12
EVOLVE_MATERIALS_IDX = 13
NO_OF_EVOLVE_TIMES_IDX = 14
COST_IDX = 17
START_SPEED_IDX = 19
ATTACK_TYPE_IDX = 20
ATTACK_FRAME_RATE_IDX = 21
HP_MIN_IDX = 25
HP_MAX_IDX = 26
HP_GAIN_IDX = 27
ATK_MIN_IDX = 32
ATK_MAX_IDX = 33
ATK_GAIN_IDX = 35
DEF_MIN_IDX = 36
DEF_MAX_IDX = 37
DEF_GAIN_IDX = 39
REC_MIN_IDX = 40
REC_MAX_IDX = 41
REC_GAIN_IDX = 43
MAX_PASSIVE_SKILLS_IDX = 46
PASSIVE1_IDX = 47
PASSIVE2_IDX = 48
PASSIVE3_IDX = 49
PASSIVE4_IDX = 50
LEADERSHIP_IDX = 51
ACTIVE_IDX = 52
SKILL_MANA_COST_IDX = 53
SKILL_DESCRIPTION_IDX = 54
# --------------------------------------------------
field_name_dict = {
    ID_IDX: '_id | (int)',
    ARCHTYPE_NAMEING_IDX: 'archtype_nameing | an (string)',
    UNIT_NAME_IDX: 'unit_name | un (string)',
    NEXT_EVOLVE_IDX: 'next_evolve | ne (string)',
    UNIT_ELEMENT_IDX: 'unit_element | ue (int)',
    MAX_LV_IDX: 'max_lv | ml (int)',
    EXP_MOD_IDX: 'exp_mod | em (int)',
    UNIT_GROWTH_IDX: 'unit_growth | ug (int)',
    RARITY_TIER_IDX: 'rarity_tier | rt (int)',
    EVOLVE_MATERIALS_IDX: 'evolve_materials | evm (int)',
    NO_OF_EVOLVE_TIMES_IDX: 'no_of_evolve_times | net (int)',
    COST_IDX: 'cost | cost (int)',
    START_SPEED_IDX: 'start_speed | ss (int)',
    ATTACK_TYPE_IDX: 'attack_type | at (int)',
    ATTACK_FRAME_RATE_IDX: 'attack_frame_rate | afr (int)',
    HP_MIN_IDX: 'hp_min | hp_min (int)',
    HP_MAX_IDX: 'hp_max | hp_max (int)',
    HP_GAIN_IDX: 'hp_gain | hp_gain (string)',
    ATK_MIN_IDX: 'atk_min | atk_min (int)',
    ATK_MAX_IDX: 'atk_max | atk_max (int)',
    ATK_GAIN_IDX: 'atk_gain | atk_gain (string)',
    DEF_MIN_IDX: 'def_min | def_min (int)',
    DEF_MAX_IDX: 'def_max | def_max (int)',
    DEF_GAIN_IDX: 'def_gain | def_gain (string)',
    REC_MIN_IDX: 'rec_min | rec_min (int)',
    REC_MAX_IDX: 'rec_max | rec_max (int)',
    REC_GAIN_IDX: 'rec_gain | rec_gain (string)',
    MAX_PASSIVE_SKILLS_IDX: 'max_passive_skills_idx | mps (int)',
    PASSIVE1_IDX: 'passive1 | pas1 (int)',
    PASSIVE2_IDX: 'passive2 | pas2 (int)',
    PASSIVE3_IDX: 'passive3 | pas3 (int)',
    PASSIVE4_IDX: 'passive3 | pas3 (int)',
    LEADERSHIP_IDX: 'leadership | ls (int)',
    ACTIVE_IDX: 'active | active (int)',
    SKILL_MANA_COST_IDX: 'skill_mana_cost | smc (int)',
    SKILL_DESCRIPTION_IDX: 'skill_description | sd (string)',
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
#element_mods_dict = {
    #'LIGHT': 8,
    #'WATER': 6,
    #'EARTH': 3,
    #'DARK': 7,
    #'AIR': 4,
    #'FIRE': 5,
#}
# ---------------------------------------------
#unit_growth_dict = {
    #'NORMAL': 1,  # default
    #'FAST': 2,
    #'SUPERB': 3,
#}
# ---------------------------------------------
#class_type_dict = { # for passive1
    #'FIGHTER': 10,
    #'DEFENDER': 11,
    #'KNIGHT': 12,
    #'GUARDIAN': 13,
    #'HERO': 14,
    #'LORD': 15,

    #'SUPER FIGHTER': 20,
    #'SUPER DEFENDER': 21,
    #'SUPER KNIGHT': 22,
    #'SUPER GUARDIAN': 23,
    #'SUPER HERO': 24,
    #'SUPER LORD': 25,

    #'ULTIMATE FIGHTER': 30,
    #'ULTIMATE DEFENDER': 31,
    #'ULTIMATE KNIGHT': 32,
    #'ULTIMATE GUARDIAN': 33,
    #'ULTIMATE HERO': 34,
    #'ULTIMATE LORD': 35,
#}
# ---------------------------------------------
start_row = 38
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
element_mods_dict = load_dict_from_sheet(book, 'Element_Mods')
unit_growth_dict = load_dict_from_sheet(book, 'Unit_Growth')
class_type_dict = load_dict_from_sheet(book, 'Class_Type')
attack_type_dict = load_dict_from_sheet(book, 'Attack_Type')
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
        val = sheet.cell_value(row, col)
        if col == UNIT_ELEMENT_IDX:
            try:
                val = element_mods_dict[val.upper()]
            except BaseException, e:
                val = 0
                #print 'execpt:' + str(e)
                #exit(0)
        elif col == UNIT_GROWTH_IDX:
            try:
                val = unit_growth_dict[val.upper()]
            except BaseException, e:
                val = 1  # default is 1 (NORMAL)

        elif col == EVOLVE_MATERIALS_IDX:
            try:
                val = bool_str_to_int_dict[val.upper()]
            except BaseException, e:
                val = 1 # default is 1 (True)

        elif col == ATTACK_TYPE_IDX:
            try:
                val = attack_type_dict[val.upper()]
            except BaseException, e:
                val = 1 # default is 1 (Melee)

        elif col == MAX_PASSIVE_SKILLS_IDX:
            try:
                val = class_type_dict[val.upper()]
            except BaseException, e:
                val = 2 # default is 2

        elif col == PASSIVE1_IDX:
            try:
                val = class_type_dict[val.upper()]
            except BaseException, e:
                val = 10 # default is 10 (FIGHTER)

        #print "row: %d, col:%d :%s" % (row, col, val)
        rec.append(val)
    print ",".join(map(str, rec))


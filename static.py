skeys = ['○', '↑', '↓',  '↓',  '←',  '↖',   '↙',    '↖',    '→',  '↗',   '↘',    '↗',    '←',    '↖',      '↙',      '↖']
kkeys = ['○', '↑', '↓', '↑↓', '←', '↑←', '↓←', '↑↓←', '→', '↑→', '↓→', '↑↓→', '←→', '↑←→', '↓←→', '←↓←→']

hmx_magicnumber=0x50523654

yym_magicnumber=0x50523754

yyc_magicnumber=0x50523854

hyz_magicnumber=0x50523954

week_array=("Sun.", "Mon.", "Tues.", "Wed.", "Thrs.", "Fri.", "Sat.")

work_attr_array={'10':[0x72303174, 0x4c, 0x50, 0x54, 0x58, 0x5c, 0x64, 0x1c4, 0x10, 0x400, 0xaa, 0xe1, 0x80, 0x3d, 0x7a, 0x8, 0x0, 10, 0x48, 0xc],
           '11':[0x72313174, 0x58, 0x5c, 0x60, 0x64, 0x68, 0x70, 0x90, 0x14, 0x800, 0xaa, 0xe1, 0x40, 0x3d, 0x7a, 0x8, 0x0, 10, 0x54, 0xc],
           '12':[0x72323174, 0x58, 0x5c, 0x60, 0x64, 0x68, 0x70, 0xa0, 0x14, 0x800, 0x5e, 0xe1, 0x40, 0x7d, 0x3a, 0x8, 0x0, 10, 0x54, 0xc],
           '13':[0x72333174, 0x58, 0x5c, 0x60, 0x64, 0x68, 0x84, 0xc4, 0x14, 0x400, 0x5c, 0xe1, 0x100, 0x7d, 0x3a, -0x8, -0x10, 10, 0x54, 0xc],
           '14':[0x72333174, 0x78, 0x7c, 0x80, 0x84, 0x88, 0xa4, 0xdc, 0x14, 0x400, 0x5c, 0xe1, 0x100, 0x7d, 0x3a, -0x8, -0x10, 10, 0x74, 0xc],
           '15':[0x72353174, 0x88, 0x8c, 0x90, 0x94, 0x98, 0xc8, 0x238, 0x14, 0x400, 0x5c, 0xe1, 0x100, 0x7d, 0x3a, -0x1c, -0x24, 10, 0x84, 0xc],
           '16':[0x72363174, 0x80, 0x84, 0x9c, 0x8c, 0x90, 0xc8, 0x294, 0x14, 0x400, 0x5c, 0xe1, 0x100, 0x7d, 0x3a, -0x20, -0x28, 10, 0x7c, 0xc],
           '128':[0x72383231, 0x58, 0x5c, 0x60, 0x64, 0x68, 0x70, 0x90, 0x14, 0x800, 0x5e, 0xe7, 0x80, 0x7d, 0x36, 0x8, 0x0, 10, 0x54, 0xc],
           '125':[0x35323174, 0x54, 0x58, 0x60, 0x64, 0x68, 0x70, 0xa0, 0x14, 0x800, 0x5e, 0xe1, 0x40, 0x7d, 0x3a, 0x8, -0x8, 1, 0x54, 0xc],
           '143':[0x33343174, 0x80, 0x84, 0x88, 0x8c, 0x90, 0xa4, 0x10c, 0x1c, 0x400, 0x5c, 0xe1, 0x100, 0x7d, 0x3a, -0x8, 0x4, 10, 0x7c, 0x14],
           '95':[0x72353974, 0x4c, 0x50, 0x2, 0x3, 0x64, 0xe8, 0x10, 0x14, 0x400, 0xaa, 0xe1, 0x80, 0x3d, 0x7a, 0x8, 0x0, 1, 0xe0, 0x10],
           '165':[0x36353174, 0x90, 0xff, 0x90, 0x8c, 0xff, 0x98, 0x08, 0x1c, 0x400, 0x5c, 0xe1, 0x100, 0x7d, 0x3a, 0xff, 0x08, 1, 0xff, 0x14],
           '17': [0x72373174, 0x84, 0x88, 0x8c, 0x90, 0x94, 0xc8, 0x158, 0x18, 0x400, 0x5c, 0xe1, 0x100, 0x7d, 0x3a, -0x20, -0x28, 10, 0x80, 0x10]}

work_attr={'10': {},
           '11': {},
           '12': {},
           '13': {},
           '14': {},
           '15': {},
           '16': {},
           '128': {},
           '125': {},
           '143': {},
           '95': {},
           '165': {},
           '17': {}}

dzz_attr=['A1-1','A1-2','A1-3','A2-2','A2-3','B1-1','B1-2','B1-3','B2-2','B2-3','C1-1','C1-2','C1-3','C2-2','C2-3','Extra','All','All','All','All','All','All','All']

def init_work_attr():
    for key, value in work_attr_array.items():
        work_attr[key]['magic_number'] = value[0]
        work_attr[key]['stage'] = value[1]
        work_attr[key]['character'] = value[2]
        work_attr[key]['ctype'] = value[3]
        work_attr[key]['rank'] = value[4]
        work_attr[key]['clear'] = value[5]
        work_attr[key]['stagedata'] = value[6]
        work_attr[key]['replaydata_offset'] = value[7]
        work_attr[key]['totalscoredata'] = value[8]
        work_attr[key]['decode_var1'] = value[9]
        work_attr[key]['decode_var2'] = value[10]
        work_attr[key]['decode_var3'] = value[11]
        work_attr[key]['decode_var4'] = value[12]
        work_attr[key]['decode_var5'] = value[13]
        work_attr[key]['decode_var6'] = value[14]
        work_attr[key]['scoredata_offset'] = value[15]
        work_attr[key]['stagedata_offset'] = value[16]
        work_attr[key]['score_rate'] = value[17]
        work_attr[key]['slowrate'] = value[18]
        work_attr[key]['date'] = value[19]
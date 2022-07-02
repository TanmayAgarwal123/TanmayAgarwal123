from earsketch import *
init()
setTempo(120)
sounds =[YG_TRAP_BRASS_1,YG_TRAP_BRASS_2,YG_TRAP_BRASS_3,YG_TRAP_BRA
SS_4,YG_TRAP_BRASS_5,HIPHOP_BASSSUB_001,RD_RNB_SFX_TONEBASS_
1,YG_NEW_HIP_HOP_BASS_1,Y07_BASS]
fitMedia(sounds[0], 1, 1, 3)
fitMedia(sounds[1], 2, 3, 6)
fitMedia(sounds[2], 3, 6, 9)
fitMedia(sounds[3], 4, 9, 12)
fitMedia(sounds[4], 5, 12, 15)
fitMedia(sounds[5], 6, 8,15)
fitMedia(sounds[6], 7, 2, 15)
fitMedia(sounds[7], 8, 1, 15)
fitMedia(sounds[8], 9, 1, 8)
setEffect( 9, VOLUME, GAIN, -30, 1, 0, 8)
finish()
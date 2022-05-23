baliqlar = {
    'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}

cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}

amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'kotex vardir',
    'yumurtlama', 'dis yoxdur'
}

surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}

quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}

sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}


#Task 1
bird_leg = quslar.add("iki ayaq")
#print(quslar)

#Task 2
fish = baliqlar.remove('4 ayaq')
#print(baliqlar)

#Task 3
cuc_am = cuculer.intersection(amfibialar)
#print(cuc_am)

#Task 4
differ = baliqlar.symmetric_difference(amfibialar)
print(differ)

#Task 5
if cuculer.isdisjoint(baliqlar) == True:
    #print('ortaq cehetleri yoxdur')
else:
    #print('ortaq cehetleri var')

#Task6
ortaq += quslar.intersection(baliqlar)
#print(len(ortaq))


#Qeyd: setleri dictionaryden almali idim, deyesen, alinmadi. vaxt qalsa baxacam gun erzinde
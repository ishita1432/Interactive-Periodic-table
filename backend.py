import csv

c1 = ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
c2 = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']
c3 = ['Sc', 'Y', 'La', 'Ac']
c4 = ['Ti', 'Zr', 'Hf', 'Rf']
c5 = ['V', 'Nb', 'Ta', 'Db']
c6 = ['Cr', 'Mo', 'W', 'Sg']
c7 = ['Mn', 'Te', 'Re', 'Bh']
c8 = ['Fe', 'Ru', 'Os', 'Hs']
c9 = ['Co', 'Rh', 'Ir', 'Mt']
c10 = ['Ni', 'Pd', 'Pt', 'Ds']
c11 = ['Cu', 'Ag', 'Au', 'Rg']
c12 = ['Zn', 'Cd', 'Hg', 'Uub']
c13 = ['B', 'Al', 'Ga', 'In', 'Tl', 'Uut']
c14 = ['C', 'Si', 'Ge', 'Sn', 'Pb', 'Uuq']
c15 = ['N', 'P', 'As', 'Sb', 'Bi', 'Uup']
c16 = ['O', 'S', 'Se', 'Te', 'Po', 'Uuh']
c17 = ['F', 'Cl', 'Br', 'I', 'At', 'Uus']
c18 = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Uuo']
c19 = ['Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']
c20 = ['Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
l = [c1, c18]
l1 = [c13, c14, c15, c16, c17]
l2 = [c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
l4 = [c19, c20]

s19_20 = []
s1_s18 = []
s2_ = []
s3_to_s12 = []
s13_17 = []

# List of colors for 1st and last column(nobel gases)
b1 = ['#b3d9ff', '#ccfff5', '#ccfff5', '#ccfff5', '#ccfff5', '#ccfff5', '#ccfff5', '#ffb3b3', '#ffb3b3', '#ffb3b3', '#ffb3b3', '#ffb3b3', '#ffb3b3', '#c2d6d6']
# List of colors for 2nd column
b2 = ['#ffb399', '#ffb399', '#ffb399', '#ffb399', '#ffb399', '#ffb399']
# List of colors for elements from 3rd to 12th column
b3 = ['#e0ccff', '#e0ccff', '#b3f0ff', '#ffc299', '#e0ccff', '#e0ccff', '#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#e0ccff','#c2d6d6','#e0ccff','#e0ccff','#e0ccff','#c2d6d6','#e0ccff','#e0ccff','#e0ccff','#c2d6d6','#e0ccff','#e0ccff','#e0ccff','#c2d6d6']
# List of colors for lanthanides and actinides
b4 = ['#b3f0ff', '#ffc299']
# List of colors for elements from 13th to 17th column
b5 = ['#ffffb3', '#b3ffe6', '#b3ffe6', '#b3ffe6', '#b3ffe6', '#c2d6d6','#b3d9ff', '#ffffb3','#ffffb3', '#b3ffe6','#b3ffe6', '#c2d6d6', '#b3d9ff', '#b3d9ff', '#ffffb3', '#ffffb3', '#b3ffe6', '#c2d6d6', '#b3d9ff', '#b3d9ff', '#b3d9ff', '#ffffb3', '#b3ffe6', '#c2d6d6', '#b3d9ff','#b3d9ff','#b3d9ff', '#b3f0ff','#b3ffe6', '#c2d6d6','#b3d9ff','#b3d9ff','#b3d9ff','#b3d9ff','#ffc299', '#c2d6d6' ]


def file1():
    with open('periodic_table.csv', mode='r') as f:
        csv_file = csv.reader(f)
        global s1,s18
        s1 = []
        s18 = []
        next(csv_file, None)

        for row in csv_file:
            for i, j in zip(c1, c18):
                if i == row[0]:
                    s1.append(row)
                if j == row[0]:
                    s18.append(row)

        s1 = s1 + s18
        for i in s1:
            s = ''
            for j in i:
                s += j
                s += ' '
            s1_s18.append(s.strip(','))
        # print(s1_s18)


def file2():
    with open('periodic_table.csv', mode='r') as f:
        csv_file = csv.reader(f)
        global s2
        s2 = []
        next(csv_file, None)
        for row in csv_file:
            for e in c2:
                if e == row[0]:
                    s2.append(row)
        for i in s2:
            s = ''
            for j in i:
                s += j
                s += ' '
            s2_.append(s.strip(','))



def file3():
    with open('periodic_table.csv', mode='r') as f:
        csv_file = csv.reader(f)
        i = 0
        global s3,s4,s5,s6,s7,s8,s9,s10,s11,s12
        s3 = []
        s4 = []
        s5 = []
        s6 = []
        s7 = []
        s8 = []
        s9 = []
        s10 = []
        s11 = []
        s12 = []
        next(csv_file, None)
        for row in csv_file:
            for y, z, k, a, m, n, o, p, q, r in zip(c3, c4, c5, c6, c7, c8, c9, c10, c11, c12):
                if y == row[0]:
                    s3.append(row)
                if z == row[0]:
                    s4.append(row)
                if k == row[0]:
                    s5.append(row)
                if a == row[0]:
                    s6.append(row)
                if m == row[0]:
                    s7.append(row)
                if n == row[0]:
                    s8.append(row)
                if o == row[0]:
                    s9.append(row)
                if p == row[0]:
                    s10.append(row)
                if q == row[0]:
                    s11.append(row)
                if r == row[0]:
                    s12.append(row)

        s3 = s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12
        for i in s3:
            s = ''
            for j in i:
                s += j
                s += ' '
            s3_to_s12.append(s.strip(','))

def file4():
    with open('periodic_table.csv', mode='r') as f:
        csv_file = csv.reader(f)
        global s13,s14,s15,s16,s17
        s13 = []
        s14 = []
        s15 = []
        s16 = []
        s17 = []
        s19 = []
        s20 = []
        next(csv_file, None)
        for row in csv_file:
            for b, c, d, h, g in zip(c13, c14, c15, c16, c17):
                if b == row[0]:
                    s13.append(row)
                if c == row[0]:
                    s14.append(row)
                if d == row[0]:
                    s15.append(row)
                if h == row[0]:
                    s16.append(row)
                if g == row[0]:
                    s17.append(row)

        s13 = s13 + s14 + s15 + s16 + s17
        for i in s13:
            s = ''
            for j in i:
                s += j
                s += ' '
            s13_17.append(s.strip(','))
        # print(s13_17)

def file5():
    with open('periodic_table.csv', mode='r') as f:
        csv_file = csv.reader(f)
        global s19, s20
        s19 = []
        s20 = []
        next(csv_file, None)
        for row in csv_file:
            for e, f in zip(c19, c20):
                if e == row[0]:
                    s19.append(row)
                if f == row[0]:
                    s20.append(row)

        s19 = s19 + s20
        for i in s19:
            s = ''
            for j in i:
                s += j
                s += ' '
            s19_20.append(s.strip(','))
        #print(s19_20)


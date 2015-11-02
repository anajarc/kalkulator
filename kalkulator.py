__author__ = 'ujarc'

try:

    stevilo_ena = float ( raw_input("vnesi prvo stevilo"))
    stevilo_dva = float ( raw_input("vnesi drugo stevilo"))
    operacija = raw_input("vnesi operacijo + - * /")


    rezultat = 0

    if operacija == "+":
        rezultat = stevilo_ena + stevilo_dva
        print rezultat
    elif operacija == "-":
        rezultat = stevilo_ena - stevilo_dva
        print rezultat
    elif operacija == "*":
        rezultat = stevilo_ena * stevilo_dva
        print rezultat
    elif operacija == "/":
        rezultat = stevilo_ena / stevilo_dva
        print rezultat

except ZeroDivisionError:
    print "Deljenje z nic ni dovoljeno"
except ValueError:
    print "Pisi samo s stevili"




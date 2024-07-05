#!/usr/bin/python3

"""Algrithms for list of integers"""


def find_peak(list_of_integers):
    if list_of_integers:
        list_of_integers.sort(revers=True)
        return list_of_integers[0]

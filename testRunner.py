from tests import *
from data import *

validList10 = generateValidDateStringList(10)
validList100 = generateValidDateStringList(100)
validList1000 = generateValidDateStringList(1000)
validList5000 = generateValidDateStringList(5000)
listWithDuplicates = generateValidListWithDuplicates(10, 5)
listWithDuplicatesMed = generateValidListWithDuplicates(10, 15)
listWithDuplicatesLong = generateValidListWithDuplicates(500,100)

invalidYears = [
    'Y199-12-30T12:34:56+12:22',
    '99-12-30T12:34:56+12:22',
    '-12-30T12:34:56+12:22'
]

invalidMonths= [
    '9999-1A-30T12:34:56+12:22',
    '9999-16-30T12:34:56+12:22',
    '9999-1-30T12:34:56+12:22',
    '9999--30T12:34:56+12:22'
]

invalidDays = [
    '9999-12-1rT12:34:56+12:22',
    '9999-12-00T12:34:56+12:22',
    '9999-12-35T12:34:56+12:22',
    '9999-12-T12:34:56+12:22'
]

invalidTimes = [
    '9999-12-30T1a:34:56+12:22',
    '9999-12-30T12:3a:5a+12:22',
    '9999-12-30T25:34:56+12:22',
    '9999-12-30T12:-1:56+12:22',
    '9999-12-30T12:34:66+12:22',
    '9999-12-30T12:34:r3+12:22',
    '9999-12-30T123:34:56+12:22',
]

invalidTimeZones = [
    '9999-12-30T12:34:56M',
    '9999-12-30T12:34:56/12:22',
    '9999-12-30T12:34:56+24:22',
    '9999-12-30T12:34:56-12:68',
    '9999-12-30T12:34:56-12:6',
    '9999-12-30T12:34:56-12::6',
]

checkAllDates(invalidTimeZones)
import codecs
import locale
import sys


def to_camel(str1):
    tmp = str1.lower()
    arr = tmp.split("_")
    arrlen = len(arr)
    # for item in arr:
    for i in range(0, arrlen):
        item = arr[i]
        item = item.capitalize()
        arr[i] = item
    return "".join(arr)


def to_camel_list(str2: str):
    arr = str2.split("\n")
    arr2 = []
    for line in arr:
        str1 = to_camel(line)
        letter = str1[0:1].lower()
        str1 = letter + str1[1:len(str1)]
        arr2.append(str1)
    return "\n".join(arr2)


if __name__ == '__main__':
    # str1 = to_camel("user_name")
    # print(str1)
    # letter = str1[0:1].lower()
    # str1 = letter + str1[1:len(str1)]
    print(to_camel_list('''ID
PROJECTNAME
ORG_NAME
ENG_NAMES
EIAFILETYPE
ACCEPTANCEDATE
NATIONALECONOMYCODE
EIAMANAGETYPE
REGION_CODE
PROJECTADDRESS
LONGITUDE
LATITUDE
PROJECTINVEST
ENVIRONINVEST
EVALUATIONUNIT
APPROVALDATE
APPROVALCODE
REPORT_QUALITY'''))
    # print(sys.getdefaultencoding())
    #
    # print(locale.getpreferredencoding());
    # print(codecs.lookup(locale.getpreferredencoding()).name)

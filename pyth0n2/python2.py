# task1
# newlist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# def number(lists):
#     result = []
#     for num in lists:
#         if num > 0 and int(num ** 0.5) ** 2 == num:
#             result.append(num)
#     return (result)
# print(f"ededler: {number(newlist)}")

 # hemcinin list comprehension ile yazdim
# newlist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# def number(lists):
#     result = [num for num in lists if num > 0 and int(num ** 0.5) ** 2 == num]
#     return (result)
# print(f"ededler: {number(newlist)}")

# -------------------------------------------------------------------------------------
# task2
# lists = [-1, 1, 2, 2, 6, 7, 7, 'say']
# def element(list):
#     newlist = []
#     for element in list:
#         if list.count(element) == 1:
#             newlist.append(element)
#     return newlist
# print(f"Təkrarlanmayan elementlər: {element(lists)}")

# hemcinin list comprehension ile yazdim
# lists = [-1, 1, 2, 2, 6, 7, 7, 'say']
# def element(lists):
#     return [element for element in lists if lists.count(element) == 1]
# print(f"Təkrarlanmayan elementlər: {element(lists)}")
# --------------------------------------------------------------------

# task3
# eded=input("ededleri daxil edin: ")
# def ededlerin_hasili(eded):
#     ededler = eded.split()
#     hasil = 1
#     for x in ededler:
#         hasil *= int(x)
#     return hasil
# result = ededlerin_hasili(eded)
# print(f"Daxil etdiyiniz edədlərin hasili: {result}")
# -----------------------------------------------------------------------------
# task4
# number = int(input("eded daxil edin: "))
# def main (number):
#     return [i for i in range(1, number + 1) if number % i == 0]
# print(f"Ədədin bölənləri: {main(number)}")
# -----------------------------------------------------------------------------

# task5
# newlist = ['may', 'iyun', 'iyul','avqust']
# def aylar(newlist):
#     return {month: len(month) for month in newlist}
# print(aylar(newlist))

# # hemcinin list comprehension ile yazdim
# newlist = ['may', 'iyun', 'iyul']
# aylar = {month: len(month) for month in newlist}
# print(aylar)
# -------------------------------------------------------------------------

# task6
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# def main(names):
#     return [name.split()[0].lower() for name in names]
# print(main(names))
# ----------------------------------------------------------------------------

# task7
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# def ortalama(nums1,list2):
#     results = []
#     for i in range(len(list1)):   
#         results.append((list1[i] + list2[i]) / 2)
#     return results
# results = ortalama(list1, list2)
# print(f"Results: {results}")


# hemcinin list comprehension ile yazdim
# list1 = [1, 2, 3]    
# list2 = [4, 5, 6]
# def ortalama(list1, list2):
#     return [(list1[i] + list2[i]) / 2 for i in range(len(list1))]
# results = ortalama(list1, list2)
# print(f"Results: {results}")
# ----------------------------------------------------------------------------------



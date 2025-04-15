# # Format Date Program

# months = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

# months_dict = {}
# for index , month in enumerate(months):
#     months_dict[month] = index + 1




# while True:
#     try:
#         data = input("Date: ")
#         if "/" in data:
#             date_arr = data.split("/")
#             month = int(date_arr[0])
#             day = int(date_arr[1])
#             year = date_arr[2]
#             if month <= 12 and day <= 31 and len(year) == 4:
#                 print(f"{year}-{month:02}-{day:02}")
#             else:
#                 continue
        
#         elif "," in data:
#             data_arr = data.replace(",","").split(" ")
#             month = months_dict[data_arr[0]]
#             day = int(data_arr[1])
#             year = data_arr[2]
#             if month <= 12 and day <= 31 and len(year) == 4:
#                 print(f"{year}-{month:02}-{day:02}")
#             else:
#                 continue

#         else:
#             print("Invalid Date Format!")
#             continue
        
        


#     except ValueError:
#         pass

#     except KeyError:
#        pass

#     else:
#         break



#  Problem 4 Grocerry List Problem
# import sys
# grocerry_dict = dict()
# while True:
#     try:
#         grocerry_item = input(" ").lower().strip()
#         grocerry_dict[grocerry_item] = grocerry_dict.get(grocerry_item,0) + 1


#     except EOFError:
#         sys.exit(0)


#     except KeyboardInterrupt:
#         for item,count in sorted(grocerry_dict.items()):
#             print(f"{count} {item.upper()}")
#         sys.exit(0)
    

#     else:
#        continue


   
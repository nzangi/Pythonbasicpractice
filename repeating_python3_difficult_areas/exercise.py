# def simple_interest(p, t, r):
#     print('The principal is', p)
#     print('The time period is', t)
#     print('The rate of interest is', r)
#
#     si = (p * t * r) / 100
#
#     print('The Simple Interest is', si)
#     return si
#
#
# # Driver code
# simple_interest(10,10,10)
# import  math
# for i in range(1,11):
#     # number = int(input("Enter a number to calculate square root:"))
#     square_root = math.sqrt(i)
#     print(square_root)
#
# for i in range(1,11):
#     if i % 2 == 0:
#         print(f"{i} is an even number")
#     else:
#         print(f"{i} is odd number")


ip = input("Enter the IP address: ")
import ipaddress

start_ip = ipaddress.IPv4Address(int(ipaddress.IPv4Address(ip) + 1))
stop_ip = ipaddress.IPv4Address(int(ipaddress.IPv4Address(ip) + 6))
for ip_address in range(int(start_ip), int(stop_ip)):
    print(ipaddress.IPv4Address(ip_address))

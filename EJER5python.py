
from xml.etree.ElementPath import findall


inicial= int(input("Digite un valor inicial:  "))
final= int(input("Digite un valor final:  "))

for i in range (inicial,final+1,1):
    if i%2==0:
        print(i)


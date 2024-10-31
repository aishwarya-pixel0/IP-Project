# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


project=pd.read_csv(r"C:\Users\sobha\Downloads\Pollution analysis ip project - Sheet1.csv")
print(project)

while(True):
    print("Main Menu")
    print("   POLLUTION ANALYSIS FOR THE YEAR 2022  ")
    print("1. Fetch data")
    print("2. Dataframe Statistics")
    print("3. Display Records")
    print("4.Bar Graph")
    print("5.Line Graph")
    print("6.. Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        project =pd.read_csv(r"C:\Users\sobha\Downloads\Pollution analysis ip project - Sheet1.csv")
    elif ch==2:
        while (True):
            print("Dataframe Statistics Menu")
            print("1. Display the Transpose")
            print("2. Display all column names")
            print("3. Display the indexes")
            print("4. Display the shape")
            print("5. Display the dimension")
            print("6. Display the data types of all columns")
            print("7. Display the size")
            print("8. Exit")
            ch2=int(input("Enter choice"))
            if ch2==1:
                print(project.T)
            elif ch2==2:
                print(project.columns)
            elif ch2==3:
                print(project.index)
            elif ch2==4:
                print(project.shape)
            elif ch2==5:
                print(project.ndim)
            elif ch2==6:
                print(project.dtypes)
            elif ch2==7:
                print(project.size)
            elif ch2==8:
                print("Let's keep our enviroNment clean and green for the next generation and work one step better every day")
                print("THANK YOU")                                             
                print("Project made by: ADITHI NARESH PISSAY AND AISHWARYA.S")
                print("Section - SR C-120")
                break

    elif ch==3:
        while(True):
            print("Display Records Menu")
            print("1. Top 4 Records")
            print("2. Bottom 4 Records")
            print("3. Specific number of records from the top")
            print("4. Specific number of records from the bottom")
            print("5. Exit")
            ch3=int(input("Enter choice"))
            if ch3==1:
                print(project.head(4))
            elif ch3==2:
                print(project.tail(4))
            elif ch3==3:
                n=int(input("Enter how many records you want to display from the top"))
                print(project.head(n))
            elif ch3==4:
                n=int(input("Enter how many records you want to display from the bottom"))
                print(project.tail(n))
            elif ch3==5: 
                print("Let's keep our enviroment clean and green for the next generation and work one step better every day")
                print("THANK YOU")                                             
                print("Project made by: ADITHI NARESH PISSAY AND AISHWARYA.S")
                print("Section - SR C-120")
                break
    elif ch==4:
         while(True):
             print("1.Bar Graph for the year 2022")
             project =pd.read_csv(r"C:\Users\sobha\Downloads\Pollution analysis ip project - Sheet1.csv")
             Country=project["COUNTRY"]
             Value=project["YEAR"]
             plt.xlabel = ("Countries")
             plt.ylabel("Values(in µg/m^3)")
             plt.title("POLLUTION ANALYSIS FOR THE YEAR 2022")
             plt.bar(Country,Value)
             plt.show()
    elif ch==5:
        while(True):
            print("Line Graph for the year 2022")
            roject =pd.read_csv(r"C:\Users\sobha\Downloads\Pollution analysis ip project - Sheet1.csv")
            Country=project["COUNTRY"]
            Value=project["YEAR"]
            plt.xlabel = ("Countries")
            plt.ylabel("Values(in µg/m^3)")
            plt.title("POLLUTION ANALYSIS FOR THE YEAR 2022")
            plt.plot(Country,Value,color='red')
            plt.show()
            
    elif ch==6:
        while(True):
            print("Let's keep our enviroment clean and green for the next generation and work one step better every day")
            print("THANK YOU")                                             
            print("Project made by: ADITHI NARESH PISSAY AND AISHWARYA.S")
            print("Section - SR C-120")
            break
            
            
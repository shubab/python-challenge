import csv

with open('Resources/budget_data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    date_list = []
    PL_list = []
    new_list = []


    for i in csv_reader:
        date_list.append(i['Date'])
        PL_list.append(int(i['Profit/Losses']))
        new_list.append(i)
  
    
    total_profit_losses = sum(PL_list)
    profit_increase = max(PL_list)
    profit_decrease = min(PL_list)
    average_change = sum(PL_list)/len(PL_list)

   

    for item in new_list:
        if int(item['Profit/Losses']) == profit_increase:
            PI_date = item['Date']
            
        
        if int(item['Profit/Losses']) == profit_decrease:
            PD_date = item['Date']


    print("Financial Analysis")
    print("-----------------------------------------------")
    print("Total Months: " + str(len(date_list)))
    print("Total: " + str(total_profit_losses))
    print("Average Change: " + str(average_change))
    print("Greatest Increase in Profits: " + PI_date +' '+ str(profit_increase))
    print("Greatest Decrease in Profits: " + PD_date +' '+ str(profit_decrease))

    

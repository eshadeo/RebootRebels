

# importing required modules
import pandas as pd
from IPython.display import display

#global goal
#goal = 0
# Functions


#Function to display information
def faq():
    print("               \n                    ------ FREQUENTLY ASKED QUESTIONS ------    \n     ")
    print("Q1  : Where can I check my previous month's saving?")
    print("----> Go to menu bar and select the option to track savings\n\n")
    print("Q2  : I have forgotten my password. What should I do?")
    print("----> Click on forgot password and enter the otp.\n\n")
    print("Q3  : I want guidance on how to save more money? What should I do?")
    print("----> Go to menu bar and select investment tips\n\n")
    print("Q4  : How to check how much money I have saved till today?")
    print("----> Go to the Menu and select option 3\n\n")
    print("Q5  : I have a question that has not been answered here.What should I do?")
    print("----> Feel free to contact us at 123456789 or reach us on email on help.sns@gmail.com\n\n")

#Function to display information
def invest_tips():
        print("            \n                      ------ EASY INVESTING ------             \n\n  ")
        print("1.Banks are the safest place to keep and grow your money!")
        print("  Create a bank account and put your money into a Fixed Deposit(FD).")
        print("  After a specific time is completed,it will give you back your money and additional amount called as interest\n\n")
        print("2.Put your money to buy small quantity of gold.Later sell the gold at higher rates\n\n")
        print("3.Invest your money in mutual funds,to know more about it,call 10101\n\n")
        print("4.Always keep aside some money from your savings to invest\n\n")
        print("5.Create a recurring FD,by adding certain deposit to your FD at regular intervals and then get back your money with interest\n\n")

#Function for woman to display loans, could be linked to bank account for updated information
def loan():
        print("  \n                                 >>> DUE LOANS <<<                 \n\n")
        print("SR N0   LOAN ISSUED FOR:-              AMOUNT TO BE PAID BACK          DEADLINE\n\n")
        print("1       Renting the harvester          ₹ 1200                         23rd Feb,2023\n")
        print("2.      Crop fertilizers               ₹ 3000                         6th May,2023\n")
        print("3.      Moneylender                    ₹ 2000                         15th May,2023\n")
        print("                                       Total : ₹ 6200            ")

#Function to add a weekly expense
def add_expense():
    expense=input("Enter expense name: ")
    amount=int(input("Enter amount: "))

    df1=pd.DataFrame(pd.read_csv('expenses.csv'))

    for index in df1.index:
        if (df1.loc[index,'Expense']).lower() == expense.lower():
            df1.loc[index, 'Amount']=df1.loc[index, 'Amount']+amount
            break

        else:
            df1.loc[len(df1.index)] = [expense, amount]
            break

    df1.to_csv('expenses.csv',index=False)


    df2=pd.DataFrame(pd.read_csv("Monthly_expense_sheet.csv"))

    df2.loc[len(df2.index)-1,'TOTAL_EXPENSE']=(df2.loc[len(df2.index)-1,'TOTAL_EXPENSE'])+amount
    df2.to_csv("Monthly_expense_sheet.csv", index=False)
    print("Successfully added ! ")

#Function to add savings for current month
def update_savings():
    goal = int(input("Enter your savings goal amount : "))
    print("Your current savings goal for the current year is : ₹", goal)
    
    df=pd.DataFrame(pd.read_csv("Monthly_expense_sheet.csv"))
    df.loc[len(df.index)-1,'SAVINGS'] = input("Enter this Month's Savings: ")
    df.to_csv("Monthly_expense_sheet.csv", index=False)
    to_goal=0
    for index in df.index:
        to_goal=to_goal+int(df.loc[index,'SAVINGS'])

    if to_goal >= goal:
        print("Congratulations ! You have reached your goal.")

    elif to_goal < goal:
        print(" ₹" ,str(goal-to_goal)+" is needed to reach your savings goal.")

#Function to add cureent month income
def update_income():
    df=pd.DataFrame(pd.read_csv("Monthly_expense_sheet.csv"))
    df.loc[len(df.index)-1,'TOTAL_INCOME'] = input("Enter this Month's Income: ")
    df.to_csv("Monthly_expense_sheet.csv", index=False)

#Function to display expenses from csv file
def display_weekly_expenses():
    df = pd.DataFrame(pd.read_csv('expenses.csv'))
    display(df)

#Function to display yearly expenditure, savings and income
def display_yearly_expenses():
    df = pd.DataFrame(pd.read_csv("Monthly_expense_sheet.csv"))
    display(df)
    print("\n\n\n\n")




#username  = "admin"   enter during runtime
#password = "123"
username  = "admin"
password = "123"
choice = 1      # initialising variable to start menu
print("      \n         ********** WELCOME TO SAVE&SPEND **********     \n\n")
print(" - Sometimes the hardest thing about saving money is just getting started - ")
print(" - This step by step guide will help you to save money and invest it -\n\n")
print(" >> Always record your expenses.\n")
print(" >> Include savings in your budget.\n")
print(" >> Set savings goals.\n")
print(" >> Determine your financial priorities.\n")
print(" >> Find ways to cut the expenses.\n")
print(" >> Watch your savings grow.\n")

#Asking user to login
username_ip = str(input("Enter Username : "))
pass_ip = str(input("Enter Password : "))
if pass_ip == password:    #checking if password is correct and proceeding

        while(choice != 9) : 
                print('''

                Menu:
                1. Add expenses for the week.
                2. Update income.
                3. Add Savings.
                4. View Loans.
                5. View yearly expenditure, savings and income.
                6. View this week's expenses.
                7. Tips on Investing, Savings.
                8. FAQ
                9. Exit  ''')
                choice = int(input("Enter your choice number : "))
                if choice == 1:
                        add_expense()
                elif choice == 2:
                        update_income()
                elif choice == 3:
                        update_savings()
                elif choice == 4:
                        loan()
                elif choice == 5:
                        display_yearly_expenses()
                elif choice == 6:
                        display_weekly_expenses()
                elif choice == 7:
                        invest_tips()
                elif choice == 8:
                        faq()
                elif choice == 9:
                        exit()
                else: 
                        print("Invalid choice, please enter a valid option.")
                        
else :    # exiting the program if password is incorrect
        print("Incorrect username or password. Please try again or click on Forgot Password")

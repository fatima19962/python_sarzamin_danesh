import cellphone
def main():
    man=input("Enter the brand of the cellphone: ")
    model=input("Enter the model of the cellphone: ")
    retail=float(input("Enter the price of the cellphone: "))
    phone=cellphone.cellphone(man,model,retail)
    print("here is data that you entered")
    print('man',phone.display_info())
main()
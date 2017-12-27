def make_car(manufacturer,model,**args):
    auto={}
    auto['manufacturer']=manufacturer
    auto['model']=model
    for key,value in args.items():
        auto[key]=value
    return auto

car=make_car('Subaru','outback',color='blue',tow_package=True)

print(car)

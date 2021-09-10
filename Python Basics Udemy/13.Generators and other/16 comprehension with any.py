from data import people,basic_plants_list,plants_list,plants_dict

if all([person[1] for person in people]):
    print("sending email")
else:
    print("missing email address no emails will be sent")

if any([plant.plant_type=="Grass" for plant in plants_list]):
    print("the pack conatins grass")
else:
    print("no grasses in the pack")

if any(plants_dict[key].plant_type=="Grass" for key in plants_dict ):
    print("this dict contains grasses")
else:
    print("no gass in the dict")
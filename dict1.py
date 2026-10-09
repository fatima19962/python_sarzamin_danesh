info_person={'name':'reza','family':'Flv','phone':'0912','Email':'test@gmail.com'}
print(info_person)
value_keys=list(info_person.keys())
value_keys.sort(reverse=True)
# value_keys.sort()
info_person_sort=dict.fromkeys(value_keys)
for key in value_keys:
    info_person_sort[key]=info_person[key]
print(info_person_sort)
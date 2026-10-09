info_person={'name':'reza','family':'Flv','phone':'0912','Email':'test@gmail.com'}
print(info_person)
list_keys=list(info_person.keys())
list_values=list(info_person.values())
info_person_reverse=dict(zip(list_values,list_keys))
print(info_person_reverse)
list_values.sort(reverse=True)
info_person_reverse_sort=dict.fromkeys(list_values)
for key in list_values:
    info_person_reverse_sort[key]=info_person_reverse[key]
print(info_person_reverse_sort)
info_person_values_sort=dict(zip(list(info_person_reverse_sort.keys()),list(info_person_reverse_sort.values())))
print(info_person_values_sort)
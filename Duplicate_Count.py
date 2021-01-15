#Counting Duplicates
def duplicate_count(text):
    adub = []
    dub = []
    for i in text:
        if not i.lower() in adub:
            adub.append(i.lower())
        else:
            dub.append(i.lower())
    return len(set(dub))
print(duplicate_count("NrDhzm5ClHr82sCh7t1H6lsGDy"))


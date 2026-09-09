items=["apple","bananna","orange","apple"];

unique_item=set()    #it store the unique value not the duplicate element.
for item in items:
    if item in unique_item:
        print("Duplicate: ",item);
        break;
    unique_item.add(item);
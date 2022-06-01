import csv
def animal_finder(animal):
    try:
        with open(f'/mnt/c/Users/kidha/Desktop/CodePlatoon/Homework_Assignments/csv-reader/data/{animal}.csv', encoding="utf-8") as f: 
            reader = csv.DictReader(f)
            for row in reader:
                print(f"{row['name']} is a{row[' age']} year old{row[' breed']}.")
    except:
        print(f"Sorry, we don't have any {animal}s here")

animal_finder('dogs')

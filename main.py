from Worker import Worker, WorkerDB
import csv

def read_workers():
    workers = WorkerDB()
    with open('/home/alona/універ/2 курс/прога/3-11./data.csv', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            name = row["name"]
            surname = row["surname"]
            department = row["department"]
            salary = float(row["salary"])
            worker = Worker(name, surname, department, salary)
            workers.add_worker(worker)
    return workers

def write(data):
    with open('/home/alona/універ/2 курс/прога/3-11./data.csv', 'r') as csv_file:
        content = csv_file.read()
    with open('/home/alona/універ/2 курс/прога/3-11./data.csv', 'w') as csv_file:
        csv_file.write(content + '\n' + data)

def add(workers):
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    worker = Worker(name, surname, department, salary)
    data = (f"{name}, {surname}, {department}, {salary}")
    workers.add_worker(worker)
    workers.print_all()
    write(data)

def sort(workers):
    while True:
        print("Choose sort:")
        print("name")
        print("surname")
        print("department")
        print("salary")
        print("3. Exit")

        choice = input("> ")
        workers.sort(choice)
        if choice == "3":
            break
        else:
            print("Wrong choice. Try again.")

def submenu(workers):
    while True:
        print("Choose an option:")
        print("1. Add worker")
        print("2. Delete worker with id")
        print("3. Sort")
        print("4. Search")
        print("5. Exit")

        choice = input("> ")
        if choice == "1":
            add(workers)
        if choice == "2":
            id = input("Enter the id: ")
            workers.delete_worker(id)
            workers.print_all()
        elif choice == "3":
            sort(workers)
        elif choice == "4":
            print()
        elif choice == "5":
            break
        else:
            print("Wrong choice. Try again.")

def main():
    workers = read_workers()
    while True:
        print("Choose an option:")
        print("1. Input data from file")
        print("2. Exit")

        choice = input("> ")
        if choice == "1":
           workers.print_all()
           submenu(workers)
        elif choice == "2":
            print("Thank you for using program")
            break
        else:
            print("Wrong choice. Try again.")

    
if __name__ == "__main__":
    main()

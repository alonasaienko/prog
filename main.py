from Worker import Worker, WorkerDB
import csv
import os

def read_workers(filename):
    workers = WorkerDB()
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            name = row["name"]
            surname = row["surname"]
            department = row["department"]
            salary = float(row["salary"])
            worker = Worker(name, surname, department, salary)
            workers.add_worker(worker)
    return workers

def write(workers,filename):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(["id", "name", "surname", "department", "salary"])

        for worker in workers.workers:
            writer.writerow([worker._Worker__id, worker.name, worker.surname, worker.department, worker.salary])

def openfile():
    while True:
        filename = input("Enter file name > ")
        try:
            if not os.path.exists(filename) or os.stat(filename).st_size == 0:
                raise ValueError
            return filename
        except ValueError:
            filename = input("Problems with file, Enter file name again >")

def add(workers,filename):
    try:
        name = (input("Enter name: "))
        surname = input("Enter surname: ")
        department = input("Enter department: ")
        if not name.isalpha() or not surname.isalpha() or not department.isalpha():
            raise ValueError(f"Skipping worker: Invalid input for name, surname, or department.") 
        salary = float(input("Enter salary: "))
        worker = Worker(name, surname, department, salary)
        workers.add_worker(worker)
    except ValueError as e:
        print(f"Skipping worker: {e}")
    workers.print_all()
    write(workers,filename)

def sort(workers):
    while True:
        print("Choose sort:")
        print("1. Name")
        print("2. Surname")
        print("3. Department")
        print("4. Salary")
        print("5. Id")
        print("6. Exit")

        choice = input("> ")

        if choice == "1":
            workers.sort("name")
        elif choice == "2":
            workers.sort("surname")
        elif choice == "3":
            workers.sort("department")
        elif choice == "4":
            workers.sort("salary")
        elif choice == "5":
            workers.sort("id")
        elif choice == "6":
            break
        else:
            print("Wrong choice. Try again.")

def submenu(workers,filename):
    while True:
        print("Choose an option:")
        print("1. Add worker")
        print("2. Delete worker with id")
        print("3. Sort")
        print("4. Search")
        print("5. Print")
        print("6. Exit")

        choice = input("> ")
        if choice == "1":
            add(workers,filename)
        if choice == "2":
            id = input("Enter the id: ")
            workers.delete_worker(id)
            workers.print_all()
        elif choice == "3":
            sort(workers)
        elif choice == "4":
            find = input("> ")
            workers.search(find)
        elif choice == "5":
            workers.print_all()
        elif choice == "6":
            break
        else:
            print("Wrong choice. Try again.")

def main():
    filename = openfile()
    workers = read_workers(filename)
    while True:
        print("Choose an option:")
        print("1. Input data from file")
        print("2. Exit")

        choice = input("> ")
        if choice == "1":
           workers.print_all()
           submenu(workers,filename)
        elif choice == "2":
            print("Thank you for using program")
            break
        else:
            print("Wrong choice. Try again.")

    
if __name__ == "__main__":
    main()

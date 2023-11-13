def decoratorsort(func):
    def __func(self):
        print("Sorted successsfully")
        result = func(self)
        print(result)
        return result
    return __func

@staticmethod
def sort(__func):
    def __sort(obj, value):
        print("Sorted successsfully")
        __func(obj, value)
    return __sort

class Worker:
    id_count = 1
    def __init__(self, name, surname, department, salary):
        Worker.id_count += 1
        self.__id = Worker.id_count
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary
    
    def __str__(self):
        return f"{self.__id}, {self.surname}, {self.name}, {self.department}, {self.salary}"
    def __rshift__(self):
        input(f"{self.name}, {self.surname}, {self.department}, {self.salary}")

class WorkerDB:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def print_all(self):
        for worker in self.workers:
            print(worker)

    def delete_worker(self, id):
        to_remove = next((worker for worker in self.workers if str(worker.id) == id), None)
        if not to_remove:
            print(f"No workers found with ID {id}.")
            return
        if to_remove:
            self.workers.remove(to_remove)
            print(f"Worker with ID {id} removed successfully!")
            return to_remove

    @sort
    def sort(self, namekey):
        return sorted(self.workers, key=lambda x: (x.str(namekey).lower(), x.str(namekey)))
    def search(self, key):
        print()
        return self.workers
    
        

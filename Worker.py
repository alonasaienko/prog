def decoratorsort(func):
    def wrapper(obj, namekey):
        print(f"Sorted successfully by {namekey}")
        result = func(obj, namekey)
        for item in result:
            print(item)
        return result
    return wrapper

def decoratorsearch(func):
    def wrapper(obj, key):
        result = func(obj, key)
        print(f"Foud successfully")
        for item in result:
            print(item)
        return result
    return wrapper
def generate(n):
    for i in range(n):
        yield i+1

class Worker:
    line_count = len('/home/alona/універ/2 курс/виробнича практика/test2/data.csv')
    id_generator = generate(line_count)
    def __init__(self, name, surname, department, salary):
        self.__id = next(Worker.id_generator)
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

    @decoratorsort
    def sort(self, namekey):
        if namekey == "salary":
            return sorted(self.workers, key=lambda x: getattr(x, namekey), reverse = True)
        if namekey == "id":
            return sorted(self.workers, key=lambda x: getattr(x, '_Worker__id'))
        else:
            return sorted(self.workers, key=lambda x: getattr(x, namekey).lower())
        
    @decoratorsearch
    def search(self, key):
        matches = []
        for item in self.workers:
            if (key.lower() in item.name.lower() or
                key.lower() in item.surname.lower() or
                key.lower() in item.department.lower() or
                (isinstance(key, float) and key == item.salary) or
                (isinstance(item.salary, float) and key in str(item.salary))):
                matches.append(item)
        return matches
    
        

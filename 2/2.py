import pickle


class Person:
    def _init_(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address


def pickle_my_list(obj_list: list):
    pickle_file = open('list.pickle', 'wb')
    pickle.dump(obj_list, pickle_file)
    pickle_file.close()


def unpickle_my_file(pickle_list_file):
    pickle_file = open('picke_list_file', 'rb')
    obj_file = pickle.load(pickle_file)
    pickle_file.close()
import addressbook_pb2


def generate_person():
    person = addressbook_pb2.Person()

    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.HOME

    return person


def serialize(person_object):
    return person_object.SerializeToString()


def deserialize(person_bytes):
    person = addressbook_pb2.Person()
    person.ParseFromString(person_bytes)
    return person


if __name__ == '__main__':
    person_obj = generate_person()

    serialized = serialize(person_obj)
    print(serialized)

    deserialized = deserialize(serialized)
    print(deserialized)

class SingletonDatabaseManager:
    __connection = None

    def __new__(cls, *args, **kwargs):
        if cls.__connection is None:
            cls.__connection = object.__new__(cls)
        return cls.__connection

    def print_connection_object_details(self):
        print(f"DB Manager Object is {id(self.__connection)}")

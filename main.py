from singleton import SingletonDatabaseManager
import time

for task in range(1, 4):
    print(f"\nTask number {task}")

    connection = SingletonDatabaseManager()
    connection.print_connection_object_details()

    time.sleep(3)


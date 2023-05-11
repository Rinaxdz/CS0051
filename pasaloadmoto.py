import threading
import multiprocessing
import time

pasaload_amount = multiprocessing.Value('i', 0)
lock = threading.Lock()

def get_phone_number():
    return input("Enter phone number: ")

def get_pasaload_amount():
    return int(input("Enter amount: "))

def perform_pasaload(phone_number, amount):
    global pasaload_amount
    print(f"Starting pasaload...")
    with lock:
        delay = 5
        print(f"Transaction will take {delay}s")
        time.sleep(delay)
        pasaload_amount.value += amount
        print(f"\nPasaload of {amount} pesos to {phone_number} is successful.")
        print(f"Current balance: {pasaload_amount.value} pesos")

if __name__ == '__main__':
    while True:
        choice = input("Proceed to Pasaload? (y/n): ").lower()
        if choice == 'y':
            phone_number = get_phone_number()
            amount = get_pasaload_amount()
            pasaload_thread = threading.Thread(target=perform_pasaload, args=(phone_number, amount))
            pasaload_thread.start()
            # pasaload_thread.join()
        elif choice == 'n':
            break
        else:
            print("Invalid choice. Please try again.")

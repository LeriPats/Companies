"""
testing module
"""
import time
import threading
class CarWash:
    """
    carwash class
    """
    def __init__(self):
        """
        carwash class
        """
        self.customers_count = threading.Semaphore(value = 2)
    def meet_customer(self, customer):
        """
        carwash class
        """
        print(f'\nInvite Customer{customer}')
        self.customers_count.acquire()
        print(f'\nWashing Customer{customer} Car')
        time.sleep(.5)
        print(f'\nCustomer{customer} Car is done')
        self.customers_count.release()
    def customers(self, count):
        """
        carwash class
        """
        for customer in range(1, count+1):
            customer_thread = threading.Thread(target = self.meet_customer, args = [customer])
            customer_thread.start()
if __name__ == '__main__':
    """
    carwash class
    """
    Visits = CarWash()
    Count = 6
    Visits.customers(Count)

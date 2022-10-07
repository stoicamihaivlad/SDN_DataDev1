from data_structures.datacenter import Datacenter
import requests
import time

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    success = False
    while not success:
        try:
            response = requests.get(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            sucess = True
        except:
            print(f'HTTP error occurred:')
            if max_retries == 0:
                return print("Maximum retries exceeded")
            max_retries -= 1
            print(max_retries)
            time.sleep(delay_between_retries) 

        else:
            print('Success!')
            return response.json()


def main():
    """
    Main entry to our program
    """

    data = get_data(URL)
    print(data)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    

    


if __name__ == '__main__':
    main()

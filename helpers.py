import requests
import json
import datetime


def send_req(url):
    # Send request
    resp = requests.get(url)

    # Decode json response
    json_response = resp.json()

    # Convert json response to dict list
    for key, value in json_response.items():
        json_to_list = value

    return json_to_list


def first_ten_image(resp):
    # Return the first 10 item of a list
    list_image = []
    for x in range(10):
        aux = resp[x]
        list_image.append(aux)
    return list_image


def calculate_earth_time(landing_time, time_to_sum):

    # https://en.wikipedia.org/wiki/Timekeeping_on_Mars day mars to seconds = 88775
    mars_seconds = int(time_to_sum) * 88775

    # Earth day to seconds = 86400
    earth_time = mars_seconds / 86400

    # Return only an integer
    time = int(earth_time)

    # Sum the earth's amount of days since the start day (landing date)
    date_aux = datetime.datetime.strptime(landing_time, "%Y-%m-%d")
    end_date = date_aux + datetime.timedelta(days=time)
    end_date = str(end_date.date())

    return end_date


def compare_list(x1, x2, x3, x4, x5, x6, x7):
    # Return max and min of a list
    list_result = [x1, x2, x3, x4, x5, x6, x7]
    max_list_photo = max(list_result)
    min_list_photo = min(list_result)
    # Create flag to return the result
    flag = False

    # Compare the max photos and min photos
    if max_list_photo > 0 & min_list_photo > 0:
        amount_photo = max_list_photo / min_list_photo

        if amount_photo > 10:
            print('the maximum number of photos is more than 10 times greater than the minimum')
            flag = False
            return flag

    elif max_list_photo > 0 & min_list_photo == 0:
        print('the maximum number of photos is more than 10 times greater than the minimum')
        flag = False
        return flag

    else:
        print('the maximum number of photos is less than 10 times that the minimum')
        flag = True
        return flag

import requests
import asyncio
from urllib.parse import urlparse

def get_ports(http_url):
    # Example HTTP URL
    # Parse the URL
    parsed_url = urlparse(http_url)
    # Get the port number (defaulting to 80 if not specified)
    port_num = parsed_url.port or 80
    # Print the port number
    return port_num

async def APICall(ip_address):
    try:
        # Make an asynchronous GET request using requests library
        response = await asyncio.to_thread(requests.get, ip_address)

        # Check if the response status code is in the 2xx range (indicating success)
        if 200 <= response.status_code < 300:
            # Read and return the response body as a string
            return response.text
        else:
            # Handle non-successful responses here if needed
            print(f"Request failed with status code: {response.status_code}")
            return None
    except Exception as e:
        # Handle exceptions here if needed
        print(f"An error occurred: {str(e)}")
        return None

def walk_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_left'))
    if response_body:
        print(f"Response Body: {response_body}")

def walk_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_right'))
    if response_body:
        print(f"Response Body: {response_body}")

def walk_forward_short(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'walk_forward_short'))
    if response_body:
        print(f"Response Body: {response_body}")

def turn_right(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'turn_right'))
    if response_body:
        print(f"Response Body: {response_body}")

def turn_left(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'turn_left'))
    if response_body:
        print(f"Response Body: {response_body}")

def sit_down(robot_motion):
    response_body = asyncio.run(APICall(robot_motion + 'sit_down'))
    if response_body:
        print(f"Response Body: {response_body}")

def standing_position(robot_motion):
    print(robot_motion + 'reset')
    response_body = asyncio.run(APICall(robot_motion + 'reset'))
    if response_body:
        print(f"Response Body: {response_body}")

def walking_position(robot_motion):
    print(robot_motion + 'basic_motion')
    response_body = asyncio.run(APICall(robot_motion + 'basic_motion'))
    if response_body:
        print(f"Response Body: {response_body}")

#use ip address from wlano0
#Boot up gray rasberry pie wait for it to say cloud login
#Press enter a few times then login when it says UXA90 login
#Name,Password is uxa90,uxa90
#IP address will be displayed in the uppder right hand corner from the device wlano0
#Append the IP address as I am below to make API calls to command the robot

def movement_command(select_command):
    session = requests.Session()
    client = session
    base_address = '10.101.142.174'
    baseIP = 'http://' + base_address
    port = 50000
    baseIP = 'http://' + base_address + ':'+str(port) + '/'
    robot_head = baseIP + 'motor?id='
    robot_motion = baseIP + 'motion/'
    if select_command == 'walk_left':
        walk_left(robot_motion)
    elif select_command == 'walk_right':
        walk_right(robot_motion)
    elif select_command == 'walk_forward_short':
        walk_forward_short(robot_motion)
    elif select_command == 'turn_right':
        turn_right(robot_motion)
    elif select_command == 'turn_left':
        turn_left(robot_motion)
    elif select_command == 'sit_down':
        sit_down(robot_motion)
    elif select_command == 'standing_position':
        standing_position(robot_motion)
    elif select_command == 'walking_position':
        walking_position(robot_motion)




#!/usr/bin/python3
import sys
import random


def calculate_subnet():
    try:
        while True:
            ip_address = input("\nEnter valid IP address: ")
            print("\nIP address type: ", type(ip_address))

            formatted_ip = string_to_list(ip_address)
            print("\nFormatted IP: ", formatted_ip)

            if (len(formatted_ip) == 4) and 1 <= formatted_ip[0] <=223 and (formatted_ip[0] != 127) and (formatted_ip[0] != 169 or formatted_ip[1] != 254) and ( 1 <= formatted_ip[1] <= 255 and 1 <= formatted_ip[2] <= 255 and 1 <= formatted_ip[3] <= 255 ):
                break
            else:
                print("\nIP address is not valid. Try again...\n")
                continue
        
        subnet_masks = [255,254, 252, 248, 240, 224, 192, 128,0]

        while True:
            ip_mask = input("\nEnter your subnet mask: ")
            print("\nIP address type: ", type(ip_mask))

            formatted_mask = string_to_list(ip_mask)
            print("\nFormatted mask: ", formatted_mask)

            if ( len(formatted_mask) == 4) and formatted_mask[0] == 255 and (formatted_mask[1] in subnet_masks and formatted_mask[2] in subnet_masks and formatted_mask[3] in subnet_masks) and (formatted_mask[0] >= formatted_mask[1] >= formatted_mask[2] >= formatted_mask[3]):
                break
            else:
                print("\nSubnet mask is not valid: ")
                continue

        binary_ip_address = convert_to_binary(formatted_ip)
        print("Binary IP address: ", binary_ip_address);
        print("Binary IP address lenght: ", len(binary_ip_address))

        binary_mask = convert_to_binary(formatted_mask)
        print("Binary subnet mask: ", binary_mask)
        print("Binary subnet mask lenght: ", len(binary_mask))

    except KeyboardInterrupt:
        print('\nProgram aborted by the user...\n')
        sys.exit()

def convert_to_binary(input_list):

    #[192, 168, 1, 10]
    bin_list = []
    counter = 0
    bin_string = ""
    #Chyba ti zatvorka kkt
    for item in input_list:
        bin_list.append((bin(input_list[counter]).split("b")[1]).zfill(8))
        counter+=1

    bin_string = "".join(bin_list);

    return bin_string



#Convert string to int list
def string_to_list(input_string):
    output_list = [];
    counter = 0
    #"255.255.255.240"
    #["255","255","255","240"]
    
    for item in input_string.split("."):
        output_list.insert(counter, int(item))
        counter+=1

    return output_list

calculate_subnet();

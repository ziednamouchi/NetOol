import random
import sys

def sub_calc():
    try:
        print("\n")

        #IP@ input and validity check
        while True:
            ip_address = input("Enter an IP address: ")

            #checking each octet validity
            octetV = ip_address.split('.')
            if (len(octetV) == 4) and (1 <= int(octetV[0]) <= 223) and (int(octetV[0]) != 127) and (int(octetV[0]) != 169 or int(octetV[1]) != 254) and (0 <= int(octetV[1]) <= 255 and 0 <= int(octetV[2]) <= 255 and 0 <= int(octetV[3]) <= 255):
                break
            else:
                print("\nThe IP address is INVALID!!! Please retry!\n")
                continue

        #checking mask validity
        mask = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        while True:
            subnet_mask = input("Enter a subnet mask: ")

            #checking each octet validity
            octetsV = subnet_mask.split('.')
            if (len(octetsV) == 4) and (int(octetsV[0]) == 255) and (int(octetsV[1]) in mask) and (int(octetsV[2]) in mask) and (int(octetsV[3]) in mask) and (int(octetsV[0]) >= int(octetsV[1]) >= int(octetsV[2]) >= int(octetsV[3])):
                break
            else:
                print("\nThe subnet mask is INVALID!!! Please retry!\n")
                continue

        mask_octet_list = []
        mask_octet_decimal = subnet_mask.split('.')

        #iterating the list
        for index in range(0, len(mask_octet_decimal)):
            binary_octet = bin(int(mask_octet_decimal[index])).split('b')[1]
            #print(binary_octet)
            if len(binary_octet) == 8:
                mask_octet_list.append(binary_octet)
            elif len(binary_octet) <8:
                bin_octet_padding = binary_octet.zfill(8)
                mask_octet_list.append(bin_octet_padding)
        #print(mask_octet_list)
        mask_octet_bin = "".join(mask_octet_list)
        #print(mask_octet_bin) ( 255.255.255.0 ====> 11111111111111111111111100000000 )

        #calculating the number of hosts per subnet
        nbr_of_zero = mask_octet_bin.count("0")
        nbr_of_one = 32 - nbr_of_zero
        nbr_of_hosts = abs(2 ** nbr_of_zero -2)
        #print(nbr_of_hosts)

        #Obtaining wildcard mask
        wildcard_octet = []
        for w_octet in mask_octet_decimal:
            wildcard = 255 - int(w_octet)
            wildcard_octet.append(str(wildcard))

        wildcard_mask = ".".join(wildcard_octet)
        #print(wildcard_mask)

        ip_addr_list = []
        ip_addr_decimal = ip_address.split('.')

        for ip_index in range(0, len(ip_addr_decimal)):
            binary_ip_octet = bin(int(ip_addr_decimal[ip_index])).split('b')[1]

            if len(binary_ip_octet) == 8:
                ip_addr_list.append(binary_ip_octet)
            elif len(binary_ip_octet) < 8:
                bin_ip_padded = binary_ip_octet.zfill(8)
                ip_addr_list.append(bin_ip_padded)

        binary_ip = "".join(ip_addr_list)
        #print(binary_ip)  (Example 1.1.1.1 ====>  0000000100000001000000010000000  )

        #obtaining the network and braodcast addresses
        network_address_binary = binary_ip[:(nbr_of_one)] + "0" * nbr_of_zero
        broadcast_address_binary = binary_ip[:(nbr_of_one)] + "1" * nbr_of_zero

        #converting network adress from bin to decimal
        net_ip_octets = []
        for n_octet in range(0, len(network_address_binary), 8):
            net_ip_octet = network_address_binary[n_octet:n_octet+8]
            net_ip_octets.append(net_ip_octet)

        net_ip_address = []
        for a_octet in net_ip_octets:
            net_ip_address.append(str(int(a_octet, 2)))

        network_address = ".".join(net_ip_address)

        # converting network adress from bin to decimal
        bst_ip_octets = []
        for b_octet in range(0, len(broadcast_address_binary), 8):
            bst_ip_octet = broadcast_address_binary[b_octet:b_octet + 8]
            bst_ip_octets.append(bst_ip_octet)

        bst_ip_address = []
        for bst_octet in bst_ip_octets:
            bst_ip_address.append(str(int(bst_octet, 2)))

        broadcast_address = ".".join(bst_ip_address)

        #print statements
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % nbr_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % nbr_of_one)
        print("\n")

        #Generation of random IP@ in subnet range
        while True:
            generate = input("Generate random ip address from subnet? (y/n)")

            if generate == "y":
                generated_ip = []

                # Obtain available IP address in range, based on the difference between octets in broadcast address and network address
                for indexb, oct_bst in enumerate(bst_ip_address):
                    # print indexb, oct_bst
                    for indexn, oct_net in enumerate(net_ip_address):
                        # print indexn, oct_net
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                # Add identical octets to the generated_ip list
                                generated_ip.append(oct_bst)
                            else:
                                # Generate random number(s) from within octet intervals and append to the list
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

                # IP address generated from the subnet pool
                # print generated_ip
                rand_addr = ".".join(generated_ip)

                print("Random IP address is: %s" % rand_addr)
                print("\n")
                continue

            elif generate == "n":
                print("Ok, bye!\n")
                break
            else:
                print("You pressed the wrong key try (y) to get a random IP@ (n) to quit!\n")


    except KeyboardInterrupt:
        print("\nProgram aborted by user. Exiting...")
        sys.exit()

#Calling the sub_calc function
sub_calc()

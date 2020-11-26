MAC ADDRESS LOOKUP TOOL 
Tool to query the https://macaddress.io/ MAC address lookup API , accepts MAC Address 
as a command line parameter and returns the Company Name associated with that MAC address

PRE REQUISITES:

Docker and Git must be installed

How to use :

1. git clone https://github.com/rucdalal/mac_lookup_container

2. cd mac_lookup_container

3. Build the container:
    ./build_container
    
4. Run container with mac-address as a parameter
    ./run_container  <mac-address>
   
   eg: ./run_container  44:38:39:ff:ef:57
    
    
Maintaining API KEY:

API KEY can be found in the environment file as 'MAC_ADDRESS_IO_API_KEY'

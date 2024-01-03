import telnetlib
import time

# Replace 'hostname' with the actual IP address or hostname of the target machine
hostname = '34.118.241.118'
port = 23  # Default Telnet port is 23

try:
    # Connect to the Telnet server
    tn = telnetlib.Telnet(hostname, port)

    # Interaction with the Telnet server
    tn.read_until(b"bezeq2 login: ")  # Modify as needed based on your Telnet server prompts
    tn.write(b"root\n")

    tn.read_until(b"Password: ")
    tn.write(b"123456\n")

    # Perform other Telnet interactions as needed
    tn.write(b"touch 1 2 3\n")
    tn.write(b"ls\n")

    # Wait for a short period to allow data to be received
    time.sleep(1)

    # Read the response
    response = tn.read_very_eager()
    print(response.decode('utf-8'))

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the Telnet connection
    tn.close()

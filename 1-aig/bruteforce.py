'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile
from zipfile import BadZipFile
# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):
#     
#
#

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            # Write your logic here...
            # Iterate through password entries in rockyou.txt
            for i in f:
            # Attempt to extract the zip file using each password
                i = i.replace(b'\n',b'')
                print("Trying pass : {}".format(i))
                try:
                    zf.extractall(path='./',pwd=i)
                    print("Password is : {}".format(i))
                    exit()
            # Handle correct password extract versus incorrect password attempt)
                except BadZipFile:
                    # continue
                    print("Error: Invalid Zip file") 
                except RuntimeError as e: 
                    # continue
                    print(f"RuntimeError: {e}") 
                except Exception as e: 
                    # continue
                    print(f"An unexpected error occurred: {e}")
            print("[+] Password not found in list")

if __name__ == "__main__":
    main()
from zipfile import ZipFile

def extract(zip , password):
    try:
        zip.extractall(pwd=password)
        return True
    except:
        return False


def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('zipname.zip') as zf:
        with open('rockyou.txt', 'rb') as f:

            for i in f:
                password = i.strip()
                if extract(zip,password):
                    print("Correct Password: %s" %password)
                    exit(0)
                
                else:
                    print("Incorrect password: %s" %password)

        print("Password not found in list")

if __name__ == "__main__":
    main()

from googlesearch import search
import sys
import time

if sys.version[0] in "2":
    print ("\n[x] gdork does not support python 2.x Use Python 3.x \n")
    exit()


class colors:
    CBLUE2 = "\33[94m"

x = ("[+] launching gdork ... \n")
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.040)
    
z = "\n"
for col in z:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.25)

try:
    data = input("\n[~] Save output to a file? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\33[94m[!] User Interruption Detected...\33[94m")
        time.sleep(0.5)
        print ("\n\33[94m[!] Quitting \33[94mn")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Name the file (file will save as .txt in current directory): ")
    print ("\n" + "  " + "-" * 50 + "\n")
    logger(data)
else:
    print ("[!] Saving skipped ...")
    print ("\n" + "  " + "-" * 50 + "\n")


def autodorks():
    try:
        dork = input("\n[~] Enter Dork Query: ")
        amount = input("[~] Enter Number of Websites to Return: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\33[94m[!] User Interruption Detected...\33[94m")
            time.sleep(0.5)
            print ("\n\33[94m[!] Quitting \33[94m\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("\n\n\33[94m[+] Google Dorking Complete\33[94m")



# =====# Main #===== #
if __name__ == "__main__":
    autodorks()

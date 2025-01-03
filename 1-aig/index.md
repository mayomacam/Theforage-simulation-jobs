﻿# Task1

### What you'll learn
* How to address a vulnerability that may affect Product Development Staging Environment infrastructure

### What you'll do
* Review some recent publications from the Cybersecurity & Infrastructure Security Agency (CISA)
* Research the reported vulnerability
* Draft an email to affected teams to alert them of the vulnerability, and explain how to remediate

---

### Here is the background information for your task
You are an Information Security Analyst in the Cyber & Information Security Team.

A common task and responsibility of information security analysts is to stay on top of emerging vulnerabilities to make sure that the company can remediate them before an attacker can exploit them. 

In this task, you will be asked to review some recent publications from the Cybersecurity & Infrastructure Security Agency (CISA). The **Cybersecurity & Infrastructure Security Agency (CISA)** is an Agency that has the goal of reducing the nation’s exposure to cyber security threats and risks. 

After reviewing the publications, you will then need to draft an email to inform the relevant infrastructure owner at AIG of the seriousness of the vulnerability that has been reported. 

---

### Here are the instructions for your task
The CISA has recently published the following two advisories:

* The [first advisory (Log4j)](https://www.cisa.gov/uscert/ncas/alerts/aa21-356a), outlines a serious vulnerability in one of the world’s most popular logging software.

* The [second advisory](https://www.cisa.gov/news/2022/02/09/cisa-fbi-nsa-and-international-partners-issue-advisory-ransomware-trends-2021) explores how ransomware has been increasing and is becoming professionalized - a concern for a large company like AIG.
Your task is to respond to the Apache Log4j zero-day vulnerability that was released to the public by advising affected teams of the vulnerability. 

**First**, conduct your research on the vulnerability using the “CISA Advisory" resources provided above as a starting point.

**Next**, analyze the “Infrastructure List” below to find out which infrastructure may be affected by the vulnerability, and which team has ownership.

			
| Product Team | Product Name | Team Lead | Services Installed | 
|-------------------------------------------|----------------------------------------------|-------------------------------------------|---------------------------------------------|
|   IT  |   Workstation Management System  |   Jane Doe (tech@email.com)  |  OpenSSH dnsmasq lighttpd  |
|   Product Development  |   Product Development Staging Environment  |  Jane Doe (product@email.com)  |   Dovecot pop3d, Apache httpd, Log4j, Dovecot imapd, MiniServ  |
|   Marketing  |   Marketing Analytics Server  |   Joe Schmoe (marketing@email.com)  |   Microsoft ftpd, Indy httpd, Microsoft Windows RPC, Microsoft Windows netbios-ssn, Microsoft Windows, Server 2008 R2 - 2012, microsoft ds  |
|   HR  |   Human Resource Information System  |   Joe Bloggs (hr@email.com)  |   OpenSSH, Apache httpd, rpcbind2-4 |

---

### Draft your advisory email below
To finish this task, draft an advisory email to alert the infrastructure owner of the seriousness of this vulnerability. 

For inspiration, you can use the email template provided below from our last cyber threat advisory.

```
From: AIG Cyber & Information Security Team
To: <affected team>
Subject: Security Advisory concerning <affected product> <affected software>
—
Body: 
Hello <affected team owner>,

AIG Cyber & Information Security Team would like to inform you that a recent <affected software> vulnerability has been discovered in the security community that may affect <affected product>.

<vulnerability description>

<vulnerability risk/impact>

<vulnerability remediation>

<any assurances to ensure advisory was actioned>

For any questions or issues, don’t hesitate to reach out to us.

Kind regards,
AIG Cyber & Information Security Team
```

#### Tips for your email:
* Make it direct and straight to the point. 
* You can assume the infrastructure owner is technical. 
* Explain the risk/impact, method of exploitation, and remediation steps.


## my mail

```
From: AIG Cyber & Information Security Team
To: Product Development Team
Subject: Security Advisory concerning Product Development Staging Environment Log4j
—
Body: 
Hello Jane Doe,

AIG Cyber & Information Security Team would like to inform you that a recent Log4j vulnerability has been discovered in the security community that may affect Product Development Staging Environment.

Description:
Log4j is a Java-based logging library used in a variety of consumer and enterprise services, websites, applications, and OT products. Recently, a vulnerability has been identified in versions Log4j 2.0-beta9 through 2.15.0 that would allow an unauthenticated attacker to perform remote code executionon affected infrastructure, making this a critical vulnerability. You can learn more in the NIST disclosures: NVD - CVE-2021-44228, NVD - CVE-2021-45046 and CVE-2021- 45105.

Risk/Impact:
Critical - remote code execution (RCE). An attacker will be able to remotely access the Product Development Staging Environment infrastructure to exfiltrate data or execute malicious actions. 

Remediation:
1. Immediately identify, mitigate, and update affected products that use Log4j to the latest patched version. 
a. For environments using Java 8 or later, upgrade to Log4j version 2.17.0 (released  December 17, 2021) or newer. 
b. For environments using Java 7, upgrade to Log4j version 2.12.3 (released December 21, 2021). Note: Java 7 is currently end of life and your team should upgrade to Java 8. 
2. Mitigate known and suspected vulnerable assets in your environment.

If you identified any signs of exploitation, please immediately reach out. After you have remediated this vulnerability, please confirm with the security team by replying to this email.
For any questions or issues, don’t hesitate to reach out to us.

Kind regards,
AIG Cyber & Information Security Team
```

### Example advisory email
Great work!

There are many ways you could have attempted this task, as advisory emails come in all shapes and sizes. Below you'll find one example of an advisory email alerting the infrastructure owner of the seriousness of this vulnerability.
```
From: AIG Cyber & Information Security Team
To: Product Development Team (product@email.com)
Subject: Security Advisory concerning Product Development Staging Environment | Log4j
—
Body:
Hello John Doe,

AIG Cyber & Information Security Team would like to inform you that a recent Log4j vulnerability has been discovered in the security community that may affect the Product Development Staging Environment infrastructure.

Vulnerability Overview
Log4j is a common open-source tool used for application logging and monitoring across the web. Recently, a vulnerability has been identified in versions Log4j2 2.0-beta9 through 2.15.0 that would allow an unauthenticated attacker to perform remote code execution on affected infrastructure, making this a critical vulnerability. You can learn more in the NIST disclosures: NVD - CVE-2021-44228 and NVD - CVE-2021-45046.

Affected products
Log4j2 2.0-beta9 through 2.15.0

Risk & Impact
Critical - remote code execution (RCE). An attacker will be able to remotely access the Product Development Staging Environment infrastructure to exfiltrate data or execute malicious actions.

Remediation
● Identify any assets or infrastructure running the affected Log4j version
● Update to the following versions: Log4j 2.16.0 (Java 8) and 2.12.2 (Java 7)
● Be on the lookout for any signs of exploitation

If you identified any signs of exploitation, please immediately reach out. After you have remediated this vulnerability, please confirm with the security team by replying to this email.

For any questions or issues, don’t hesitate to reach out to us.

Kind regards,
AIG Cyber & Information Security Team
```

---
---

# Task 2

### What you'll learn
* What ‘bruteforcing’ involves
* How to respond to a ransomware virus using Python

### What you'll do
* Write a Python script to bruteforce the decryption key of the encrypted file, to avoid paying a ransom

---

### Setting the scene for your next task
Your advisory email in the last task was great. It provided context to the affected teams on what the vulnerability was, and how to remediate it. 

Unfortunately, an attacker was able to exploit the vulnerability on the affected server and began installing a ransomware virus. Luckily, the Incident Detection & Response team was able to prevent the ransomware virus from completely installing, so it only managed to encrypt one zip file. 

Internally, the Chief Information Security Officer does not want to pay the ransom, because there isn’t any guarantee that the decryption key will be provided or that the attackers won’t strike again in the future. 

Instead, we would like you to bruteforce the decryption key. Based on the attacker’s sloppiness, we don’t expect this to be a complicated encryption key, because they used copy-pasted payloads and immediately tried to use ransomware instead of moving around laterally on the network.

---

### Here is the background information for your task
In this task, you will write a Python script to bruteforce the decryption key of the encrypted file.

Bruteforcing is the act of repeatedly trying different combinations to break the password encryption (based on either randomly generated passwords, or from a list of passwords to try). In the resource below, we've provided a small subset of passwords from Rockyou - a widely know password wordlist that contains thousands of common passwords in one wordlist.

Ransomware will often encrypt all files on a device, and sometimes give the decryption key after the ransom has been paid (but this is not always the case!). In this task, we would like you to break the encryption without paying the ransom.

A foundational Python 3+ template has also been provided for you in the resource below. One potential implementation is described in the code comments.

![Download zip here!](https://cdn.theforage.com/vinternships/companyassets/4nAmAbTbHbnGMNSyo/xC9sB8pSNLiDsK7vp/1645636758345/EncryptedFilePack.zip)

After, open the decrypted word doc and paste your Python code in the text field below. We'll show you an example answer on the next step, but we encourage you to give it a go first!

## My code 
```
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
```

### Sample code
Great work! Here is a sample Python script to bruteforce the decryption key of the encrypted file. 
```
from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for p in f:
                password = p.strip()
                if attempt_extract(zf, password):
                    print("[+] Correct password: %s" % password)
                    exit(0)
                else:
                    print("[-] Incorrect password: %s" % password)

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
```
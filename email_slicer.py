#input for email id

email = input("Enter the email id: ").strip()

username = email[:email.index("@")]

domain = email[email.index("@")+1:email.index(".")]

output = "your usename is {} and your domain is {}".format(username,domain)

print(output)

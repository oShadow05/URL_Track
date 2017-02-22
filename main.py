from time import strftime, localtime
def print_URL( url):
    print('URL GET FOR NOW:\n')
    """ cicle for print the url of _x_ index """
    for x in url.keys():
        print ("Name: ", x, "\tUrl: ", url[x])



def add_URL(url, name, website):
     url[name] = website





def lookup_URL(urls, name):
    if name not in urls :
        return name + " was not found"

    else:
        return "The website is " + urls[name]





def remove_URL(urls, name):
    if name not in urls:
        print(name, " was not found")
    else:
        del urls[name]





def save_URL(urls, list_URL):
    out_file = open(list_URL + ".txt", "a")
    for i in urls.keys():
        out_file.write(i + ", " + urls[i] + "                       " + strftime("%H:%M:%S", localtime()) + "                          " + strftime("%A.%d/%b/%y", localtime()) + "\n")
    out_file.close()



def print_menu():
    print('1. Print URL ')
    print('2. Add a URL')
    print('3. Lookup a URL')
    print('4. Remove a URL')
    print('5. Save URLs')
    print('6. Quit')

url_list = {}
print_menu()
action_number = 0

while action_number!=6:
        action_number = int(input("Your choose is... "))
        if action_number == 1:
            print_URL(url_list)

        elif action_number == 2:
              name = input("Name: ")
              url = input("URL: ")
              add_URL(url_list, name, url)

        elif action_number == 3:
            print("Lookup number ")
            name = input("Name: ")
            print(lookup_URL(url_list, name))

        elif action_number == 4:
             name = input("Name: ")
             remove_URL(url_list, name)


        elif action_number == 5:
            filename2 = input("Filename to save:")
            save_URL(url_list, filename2)














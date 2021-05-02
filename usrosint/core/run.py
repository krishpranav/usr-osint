from usrosint.core.colors import Colors
import threading

def run(self):
    self.print_logo()

    # No argument
    if not len(self.items):
        print('''usr-osint is an OSINT tool that allows you to find potential profiles of a person on social networks, as well as their email addresses and shows you the data leak of the found emails.
    Usage : ./usrosint.py <arguments>
    for exemple : ./usrosint.py user name
                ./usrosint.py user name''')

    else:
        self.menu()
        self.get_permutations()

        # Number of permutations to test per service
        print(Colors.BOLD + "[+]" + Colors.ENDC + " {} permutations to test for each service, you can reduce this number by selecting less options if it takes too long".format(len(self.permutations_list)))

        modules = self.get_report_modules()

        print("\n" + "usrosint will search : \n " + Colors.BOLD + "[+] " + Colors.ENDC +  "{} \n".format(str('\n ' + Colors.BOLD + "[+] " + Colors.ENDC).join(modules)))

        for module in modules:
            thread = threading.Thread(target=self.modules[module]["method"])
            thread.start()
            thread.join()
        self.generate_report()
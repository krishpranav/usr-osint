from usrosint.modules.tchat.skype import Skype

# Skype
def skype(self):
    self.result["skype"] = Skype(self.CONFIG, self.permutations_list).search() 
    self.print_results("skype")
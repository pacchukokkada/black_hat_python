import os
 
 def run(**args):
     print("[*] In irlister modules")
     files = os.listdir(".")

     return str(files)
     
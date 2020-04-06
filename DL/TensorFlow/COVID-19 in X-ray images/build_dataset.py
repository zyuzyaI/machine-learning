from imutils import paths
import pandas as pd 
import numpy as np
import shutil
import os

class MadeTwoClasses:

    def copy_file(self, lst_name, name):
        try:
            for f in lst_name:
                shutil.copy(os.getcwd()+"/images/"+f, (os.getcwd()+"/dataset/{}/"+f).format(name))
        except:
            print ("[INFO] Copy to the directory %s failed" % name)
        else:
            print ("[INFO] Copy to the directory %s " % name)
        

    def build(self, df):
        PATH = os.getcwd()
        print("[INFO] Current directory: ", PATH)
        for path_name in ("/dataset/normal/", "/dataset/covid/"):
            create_path = PATH + path_name
            try:
                os.mkdir(create_path)
            except OSError:
                print ("[INFO] Creation of the directory %s failed" % create_path)
            else:
                print ("[INFO] Successfully created the directory %s " % create_path)

        no_covid = []
        covid = []
        for _, col in df.iterrows():
            if col["finding"] != "COVID-19" or col["view"] != "PA":
                no_covid.append(col["filename"])
                continue
            else:
                covid.append(col["filename"])

        # copy image to directory
        self.copy_file(no_covid, "normal")
        self.copy_file(covid, "covid")
         

if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\Irka\web\pyimage\COVID-19 in X-ray images\metadata.csv")
    mtc = MadeTwoClasses()
    mtc.build(df)  

# Pythono3 code to rename multiple 
# files in drawables folders in android projects 

# imports
import os 
import sys
import re


# Function to rename multiple files 
def main(project_path): 
    directories = os.listdir(project_path)
    for directory in directories:
        print(directory)
        if(directory.startswith('drawable')):
            print("processing dir: " + directory +" ...")
            path = os.path.join(project_path,directory)
            if os.path.isdir(path):
                for filename in os.listdir(path): 
                    ## check if the file name begins with numbers 
                    f = re.findall(r'^\d+\.?\d*?_',filename)
				
		    ## save the src path
                    src = os.path.join(path, filename)
                    num = ''
                    ## get file name without extension and its extension
                    file, extension = os.path.splitext(os.path.basename(filename))
                    new_name = file
                    if f:
                        ## remove the numbers from the beginig 
                        new_name = filename[len(f[0]):]
                        ## get the number
                        num = '_'+f[0][:-1]

                    ## replace the '.' & '-' in the file name with '_'
                    new_name = new_name.split(extension)[0].replace('.','_').replace('-','_')+num+extension
                    new_name = new_name.lower()
                    if new_name != filename:
                        os.rename(src, os.path.join(path,new_name))  
                        print('renamed from: '+filename + ' to : '+new_name)
			
                        print(directory + " processed!!")
            else:
                print('dir: ' + directory + ' does not exists!!!')

# Driver Code 
if __name__ == '__main__': 
    # Calling main() function 
    project_dir = os.path.join(sys.argv[1],"app/src/main/res/")
    main(project_dir) 

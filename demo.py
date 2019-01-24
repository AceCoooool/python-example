import os  # Load the Library Module
from time import strftime  # Load just the strftime Module from Time

logsdir = "./logs"  # Set the Variable logsdir
zip_program = "zip"  # Set the Variable zip_program - 1.1

logsdir = os.path.abspath(logsdir)

# for file in os.listdir(logsdir):  # Find all the files in the directory
#     if file.endswith(".log"):  # Check to ensure the files in the directory end in .log
#         files1 = file + "." + strftime(
#             "%Y-%m-%d") + ".zip"  # Create the Variable files1, this is the files in the directory, then we add a suffix with the date and the zip extension
#         os.chdir(logsdir)  # Change directory to the logsdir
#         os.system(zip_program + " " + files1 + " " + file)  # Zip the logs into dated zip files for each server. - 1.1
#         os.remove(file)  # Remove the original log files

filename = 'logzip'
p = os.listdir(logsdir)

os.system('zip' + " " + "file.zip" + " " + ' '.join(['logs/1.log', 'logs/2.log']))



import os
import sys
import wget
import tarfile
import shutil
from azure.devops.agent import task

def run():
    try:
        # Get inputs
        download_url = task.get_input('downloadUrl', required=True)
        output_directory = task.get_input('outputDirectory', required=True)

        # Create output directory if it does not exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Download the file
        file_name = os.path.join(output_directory, 'downloaded.tar')
        wget.download(download_url, file_name)

        # Extract the tar file
        with tarfile.open(file_name, 'r') as tar:
            tar.extractall(path=output_directory)

        # Cleanup downloaded tar file
        os.remove(file_name)

        # Log success
        print(f'Downloaded and extracted tar file from {download_url} to {output_directory}')
        task.set_result(task.TaskResult.Succeeded)

    except Exception as err:
        task.set_result(task.TaskResult.Failed, str(err))

if __name__ == '__main__':
    run()

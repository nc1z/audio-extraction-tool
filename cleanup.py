import subprocess

def remove_output_parts_directory():
    try:
        subprocess.run(["rm", "-rf", "./output_samples"])
        print("Successfully removed the output_samples directory.")
    except Exception as e:
        print(f"Error removing output_samples directory: {str(e)}")

remove_output_parts_directory()

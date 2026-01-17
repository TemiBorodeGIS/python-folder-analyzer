print("SCRIPT STARTED")
import os
def analyze_folder(folder_path):
    print("Analyzing folder:", folder_path)
    file_counts = {}

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()

            if ext == '':
                ext = 'no_extension'

                file_counts[ext]= file_counts.get(ext, 0) + 1
    return file_counts


def save_report(report, output_file):
    with open(output_file, 'w') as f:
        f.write("Folder Analysis Report\n")
        f.write("======================\n")

        for ext, count in report.items():
            f.write(f"{ext}: {count} files\n")

if __name__ == "__main__":
    print("MAIN BLOCK RUNNING")

    folder = "data"
    output = "analysis_report.txt"

    results = analyze_folder(folder)
    print("Results:", results)

    save_report(results, output)

    print("DONE")
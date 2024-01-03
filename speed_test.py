import os
import speedtest
import time
import csv

def run_speedtest_and_log_to_csv():
    s = speedtest.Speedtest()
    
    # Convert speeds to megabytes per second (MBps)
    download_speed = s.download() / 1000000 / 8  # Convert to MBps
    upload_speed = s.upload() / 1000000 / 8  # Convert to MBps
    
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # Format timestamp

    # Print to stdout
    print(f'Timestamp: {current_time}, Download Speed: {download_speed:.2f} MBps, Upload Speed: {upload_speed:.2f} MBps')

    csv_file_path = 'speedtest_results.csv'

    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        # If the file doesn't exist, print headers and create the CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Timestamp', 'Download Speed (MBps)', 'Upload Speed (MBps)'])

    # Open CSV file in append mode and write data
    with open(csv_file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([current_time, download_speed, upload_speed])  # Write row to CSV

# Run the script for 5 iterations with a 60-second delay
for i in range(5):
    run_speedtest_and_log_to_csv()
    time.sleep(60)

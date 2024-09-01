import os
import argparse
import subprocess
import paramiko
from getpass import getpass
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description='Run communication benchmark tests.')
    
    # Dynamically add arguments based on the parameters passed from run_dpdbento.py (TCP/RDMA/DMA)
    parser.add_argument('--benchmark_items', type=str, required=True, help='Comma-separated list of benchmark items')
    
    # Add all possible parameters; any unused will remain default
    parser.add_argument('--data_size', type=int, default=8, help='Bytes to transfer')
    parser.add_argument('--queue_depth', type=int, default=1, help='Queue depth')
    parser.add_argument('--threads', type=int, default=1, help='Number of threads')
    parser.add_argument('--test_rounds', type=int, default=100, help='Total number of transfers')
    parser.add_argument('--host_ib_dev', type=str, default="e1:00.1", help='PCI address of host')
    parser.add_argument('--dpu_ib_dev', type=str, default="03:00.1", help='PCI address of DPU')
    parser.add_argument('--host_ip', type=str, default="10.70.60.11", help='IP address of host')
    parser.add_argument('--host_username', type=str, default="annali", help='username of host')
    parser.add_argument('--dpu_ip', type=str, default="192.168.100.2", help='IP address of dpu')
    parser.add_argument('--port', type=int, default=8080, help='Port number')
    
    return parser.parse_args()

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def tcp_ssh_into_host_run_server_and_client(hostip, username, port, file_size, threads, total_requests, log_file, output_file):
    
    # file path to the tcp folder 
    file_path = os.path.join(os.path.dirname(__file__), "tcp")

    # path to the shell script that initiates the ssh connection to host, starts the server on host, and ssh back to dpu to start client side on dpu
    shell_script = os.path.join(file_path, "client.sh")
    
    # outputs the echo commands from shell script to the log file
    with open(log_file, 'w') as log:
        command = ["bash", shell_script, username, hostip, port, file_size, threads, total_requests, output_file]
        subprocess.run(command, stdout=log, stderr=log, text=True)

def rdma_ssh_into_host_run_server_and_client(hostip, username, port, file_size, threads, total_requests, log_file, output_file):
    pass

def run_benchmark(port, data_size, queue_depth, threads, test_rounds, host_pci, dpu_pci, host_username, host_ip, dpu_ip, output_folder, log_file, benchmark_item):
    print(f"Running {benchmark_item} test with block_size={data_size} bytes, queue depth={queue_depth}, threads={threads}, test_rounds={test_rounds}", file=log_file)
    
    test_run_dir = os.path.join(output_folder, benchmark_item, f"{data_size}_{queue_depth}_{threads}_{test_rounds}")
    create_directory(test_run_dir)    
    
    temp_output_file = os.path.join(test_run_dir, f"output.csv")
    
    if benchmark_item == "TCP":
        tcp_ssh_into_host_run_server_and_client(host_ip, host_username, port, data_size, threads, test_rounds, log_file, temp_output_file)
        
        print(f"SSH to host completed. Server on host started. Client on DPU started. File Transfer complete.", file=log_file)
        print(f"Results saved to {temp_output_file}", file=log_file)
        
    if benchmark_item == "RDMA":
        rdma_ssh_into_host_run_server_and_client(host_ip, host_username, port, data_size, threads, test_rounds, log_file, temp_output_file)
        
        print(f"SSH to host completed. Server on host started. Client on DPU started. File Transfer complete.", file=log_file)
        print(f"Results saved to {temp_output_file}", file=log_file)
        
   
def main():
    args = parse_arguments()
    
    communication_output_dir = os.path.join(os.path.dirname(__file__), 'output')
    create_directory(communication_output_dir)
    
    log_file_path = os.path.join(communication_output_dir, "benchmark_test_log.txt")
    
    with open(log_file_path, 'a') as log_file:
        benchmark_items = args.benchmark_items.split(',')

        for benchmark_item in benchmark_items:
            run_benchmark(args.port, args.data_size, args.queue_depth, args.threads, args.test_rounds, args.host_pci, args.dpu_pci, args.host_ip, args.dpu_ip, communication_output_dir, log_file, benchmark_item)
    
if __name__ == '__main__':
    main()
    print(f"Finished running communication benchmarks")
    
import argparse
import requests
import time

parser = argparse.ArgumentParser(description='Hit an endpoint and return information and statistics about response times, bytes sent, and so on.')
parser.add_argument('--url', required=True, help='URL of the endpoint to hit')
parser.add_argument('--num_requests', type=int, default=10, help='Number of times to hit the endpoint')
parser.add_argument('--timeout', type=float, default=1, help='Timeout value for each request')

args = parser.parse_args()

def hit_endpoint():
    try:
        start_time = time.time()
        response = requests.get(args.url, timeout=args.timeout)
        end_time = time.time()

        response_time = end_time - start_time
        bytes_sent = len(response.content)

        return response_time, bytes_sent
    except requests.exceptions.Timeout:
        return None, None

response_times = []
bytes_sent_list = []
for i in range(args.num_requests):
    response_time, bytes_sent = hit_endpoint()
    if response_time is None:
        print(f"Request {i+1}: Timeout")
    else:
        response_times.append(response_time)
        bytes_sent_list.append(bytes_sent)
        print(f"Request {i+1}: {response_time:.3f}s, {bytes_sent} bytes")

if response_times:
    print(f"\nAverage response time: {sum(response_times)/len(response_times):.3f}s")
    print(f"Average bytes sent: {sum(bytes_sent_list)/len(bytes_sent_list):.3f} bytes")

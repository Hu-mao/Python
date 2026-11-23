
import time


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # Інформація про запит
        print("\n========== HTTP REQUEST ==========")
        print(f"Method: {request.method}")
        print(f"URL: {request.get_full_path()}")

        # Cookie без csrf
        cookies = {
            key: value
            for key, value in request.COOKIES.items()
            if key != "csrftoken"
        }

        print(f"Cookies: {cookies}")

        response = self.get_response(request)

        # Час виконання
        duration = time.time() - start_time

        print(f"Execution time: {duration:.4f} seconds")
        print("================================\n")

        return response

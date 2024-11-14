import axios, { AxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';
import { toast } from 'vue3-toastify';
import { useRouter } from 'vue-router';


const apiClient = axios.create({
  baseURL: process.env.VITE_API_URL || "http://localhost:8000/v1",
  timeout: 1000,
  headers: {
    "Content-Type": "application/x-www-form-urlencoded"
  },
});

// Request interceptor example: Adding an authorization token
apiClient.interceptors.request.use((config: AxiosRequestConfig |  any) => {
  const token = localStorage.getItem('access');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, function (error) {
  // Do something with request error
  toast.error("Error Notification !", {
    position: "top-left"
  });

  return Promise.reject(error);
});

// Create a function to refresh the token
const refreshAccessToken = async () => {
  const refreshToken = localStorage.getItem('refresh_token');
  if (!refreshToken) {
    return Promise.reject('No refresh token available');
  }

  try {
    const response = await axios.post(`${process.env.VITE_API_URL || "http://localhost:8000/v1"}/auth/token/refresh`, {
      refresh: refreshToken,
    });

    const newAccessToken = response.data.access;
    const newRefreshToken = response.data.refresh;

    // Store the new tokens
    localStorage.setItem('access', newAccessToken);
    localStorage.setItem('refresh_token', newRefreshToken);

    return newAccessToken;
  } catch (error) {
    console.error('Failed to refresh token:', error);
    toast.error('Session expired. Please login again.');
    return Promise.reject(error);
  }
};


// Response interceptor example: Handling errors
apiClient.interceptors.response.use(
  (response: AxiosResponse) => response, 
  async (error: AxiosError) => {
    const router = useRouter();

    if (error.response) {
      const { status } = error.response;
      const originalRequest: AxiosRequestConfig = error.config; // Store the original request
      if (status === 401 && originalRequest && !originalRequest._retry) {
        // Check if originalRequest exists and has not been retried
        originalRequest._retry = true;
        try {
          const newAccessToken = await refreshAccessToken();

          // Retry the original request with the new access token
          originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;
          return apiClient(originalRequest); // Retry the failed request
        } catch (refreshError) {
          toast.error('You need to login again!');
          localStorage.removeItem('access');
          localStorage.removeItem('refresh_token');
          router.push('/login'); // Redirect to login if refresh token fails
        }
      }

      if (error.response.data && error.response.data.detail) {
        toast.error(error.response.data.detail);
      }
    }

    return Promise.reject(error);
  }
);


export default apiClient;
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

// Response interceptor example: Handling errors
apiClient.interceptors.response.use(
  (response: AxiosResponse) => response, 
  (error: AxiosError) => {
    const router = useRouter();
    if (error.response) {
      let response: any = error.response
      if (response?.status === 401) {
        toast.error('You need login!')
        localStorage.setItem('access', '');
        router.push('/login');
      }
      toast(response.data.detail)
    }
    return Promise.reject(error); 
  }
);


export default apiClient;
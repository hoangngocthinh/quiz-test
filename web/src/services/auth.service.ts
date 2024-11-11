import axios from 'axios';

const API_URL: String = import.meta.env.VITE_API_URL


class AuthService {
    login(user: any) {
        return axios
        .post(API_URL + '/auth/token/', {
            username: user.username,
            password: user.password
        })
        .then(response => {
            if (response.data.accessToken) {
                localStorage.setItem('user', JSON.stringify(response.data));
            }

            return response.data;
        });
    }

    logout() {
        localStorage.removeItem('user');
    }

    register(user: any) {
        return axios.post(API_URL + '/auth/registration/', {
            username: user.username,
            email: user.email,
            password: user.password
        });
    }
}

export default new AuthService();